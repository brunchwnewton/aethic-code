#!/usr/bin/env python3
"""Run steps 3 to 7 of the pipeline in order: the offline part, from the scraped duels to every file in outputs/.

Usage:  python3 run_3_to_7.py [duels.csv] [--from N] [--to N]

Each step runs as its own script from this folder, exactly as the README's commands do, so this works from any
directory. The duels file (default: duels.csv in this folder) goes to steps 3 and 7, the two that read it; the other
steps read the previous step's results in outputs/. The run stops at the first step that fails. --from and --to run
part of the chain: --from 5 after changing step 5, say, reuses the outputs of steps 3 and 4."""
import argparse, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = {  # step: (script, whether it takes the duels file)
    3: ('3_bt_fit.py', True),
    4: ('4_categorize.py', False),
    5: ('5_rescale_dinos.py', False),
    6: ('6_curve_fit.py', False),
    7: ('7_cultural_inflation.py', True),
}


def main():
    ap = argparse.ArgumentParser(description='Run steps 3 to 7 of the pipeline in order.')
    ap.add_argument('duels', nargs='?', help='the scraped duels file (default: duels.csv in this folder)')
    ap.add_argument('--from', dest='first', type=int, choices=sorted(STEPS), default=3, help='first step to run (default 3)')
    ap.add_argument('--to', dest='last', type=int, choices=sorted(STEPS), default=7, help='last step to run (default 7)')
    args = ap.parse_args()
    if args.first > args.last:
        ap.error('--from must not come after --to')
    duels = Path(args.duels).resolve() if args.duels else HERE / 'duels.csv'
    if not duels.is_file():
        ap.error(f'duels file not found: {duels}')

    start = time.time()
    for n in range(args.first, args.last + 1):
        script, takes_duels = STEPS[n]
        cmd = [sys.executable, script] + ([str(duels)] if takes_duels else [])
        print(f'\n=== step {n}: {script}', flush=True)
        t = time.time()
        if subprocess.run(cmd, cwd=HERE).returncode:
            sys.exit(f'\nstep {n} ({script}) failed; the steps after it were not run')
        print(f'=== step {n} done in {time.time() - t:.1f} s', flush=True)
    done = f'step {args.first}' if args.first == args.last else f'steps {args.first} to {args.last}'
    print(f'\n{done} done in {time.time() - start:.1f} s; results in {HERE / "outputs"}')


if __name__ == '__main__':
    main()
