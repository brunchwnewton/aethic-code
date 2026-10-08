import java.util.Scanner; 
public class Elements {
	public static boolean findEle(char in1, char in2) {
		String TABLE="H_0He0Li0Be0B_0C_0N_0O_0F_0Ne0Na0Mg0Al0Si0P_0S_0Cl0Ar0K_0Ca0Sc0Ti0V_0Cr0Mn0Fe0Co0Ni0Cu0Zn0Ga0Ge0As0Se0Br0Kr0Rb0Sr0Y_0Zr0Nb0Mo0Tc0Ru0Rh0Pd0Ag0Cd0In0Sn0Sb0Te0I_0Xe0Cs0Ba0La0Ce0Pr0Nd0Pm0Sm0Eu0Gd0Tb0Dy0Ho0Er0Tm0Yb0Lu0Hf0Ta0W_0Re0Os0Ir0Pt0Au0Hg0Tl0Pb0Bi0Po0At0Rn0Fr0Ra0Ac0Th0Pa0U_0Np0Pu0Am0Cm0Bk0Cf0Es0Fm0Md0No0Lr0Rf0Db0Sg0Bh0Hs0Mt0Ds0Rg0Cn0Nh0Fl0Mc0Lv0Ts0Og0000";
		int place=0;
		boolean compl=false;
		while ((!(place==354))&&(!(compl))) {
			if ((Character.toUpperCase((TABLE.charAt(place)))==Character.toUpperCase(in1))&&(Character.toUpperCase((TABLE.charAt((place)+1)))==Character.toUpperCase(in2))) {
				compl=true;
				return compl;
			}else{
				place=place+3;
			}
		}
		return compl;
	}
	public static String placeEle(int in1) {
		String TABLE="H_0He0Li0Be0B_0C_0N_0O_0F_0Ne0Na0Mg0Al0Si0P_0S_0Cl0Ar0K_0Ca0Sc0Ti0V_0Cr0Mn0Fe0Co0Ni0Cu0Zn0Ga0Ge0As0Se0Br0Kr0Rb0Sr0Y_0Zr0Nb0Mo0Tc0Ru0Rh0Pd0Ag0Cd0In0Sn0Sb0Te0I_0Xe0Cs0Ba0La0Ce0Pr0Nd0Pm0Sm0Eu0Gd0Tb0Dy0Ho0Er0Tm0Yb0Lu0Hf0Ta0W_0Re0Os0Ir0Pt0Au0Hg0Tl0Pb0Bi0Po0At0Rn0Fr0Ra0Ac0Th0Pa0U_0Np0Pu0Am0Cm0Bk0Cf0Es0Fm0Md0No0Lr0Rf0Db0Sg0Bh0Hs0Mt0Ds0Rg0Cn0Nh0Fl0Mc0Lv0Ts0Og0000";
		String rough="";
		if ((TABLE.charAt((in1*3)+1))=='_') {
			rough=String.valueOf(TABLE.charAt(in1*3));
		}else {
			rough=String.valueOf(TABLE.charAt(in1*3)) + String.valueOf((TABLE.charAt((in1*3)+1)));
		}
		return rough;
	}
	public static String placeEleUpper(int in1) {
		String TABLE="H_0He0Li0Be0B_0C_0N_0O_0F_0Ne0Na0Mg0Al0Si0P_0S_0Cl0Ar0K_0Ca0Sc0Ti0V_0Cr0Mn0Fe0Co0Ni0Cu0Zn0Ga0Ge0As0Se0Br0Kr0Rb0Sr0Y_0Zr0Nb0Mo0Tc0Ru0Rh0Pd0Ag0Cd0In0Sn0Sb0Te0I_0Xe0Cs0Ba0La0Ce0Pr0Nd0Pm0Sm0Eu0Gd0Tb0Dy0Ho0Er0Tm0Yb0Lu0Hf0Ta0W_0Re0Os0Ir0Pt0Au0Hg0Tl0Pb0Bi0Po0At0Rn0Fr0Ra0Ac0Th0Pa0U_0Np0Pu0Am0Cm0Bk0Cf0Es0Fm0Md0No0Lr0Rf0Db0Sg0Bh0Hs0Mt0Ds0Rg0Cn0Nh0Fl0Mc0Lv0Ts0Og0000";
		String rough="";
		if ((String.valueOf(TABLE.charAt((in1*3)+1))).equals("_")) {
			rough=String.valueOf(Character.toUpperCase(TABLE.charAt(in1*3)));
		}else {
			rough=String.valueOf(Character.toUpperCase(TABLE.charAt(in1*3))) + String.valueOf(Character.toUpperCase((TABLE.charAt((in1*3)+1))));
		}
		return rough;
	}
	public static char Long(String word, int let) {
		if (word.length()>3) {
			return word.charAt(let);
		}else {
			if ((word.length()<let+1)) {
				return '_';
			}else {
				return word.charAt(let);
			}
		}
	}
	public static String nameIt(int ord) {
		String fullTable="001Hydrogen002Helium003Lithium004Beryllium005Boron006Carbon007Nitrogen008Oxygen009Fluorine010Neon011Sodium012Magnesium013Aluminum014Silicon015Phosphorus016Sulfur017Chlorine018Argon019Potassium020Calcium021Scandium022Titanium023Vanadium024Chromium025Manganese026Iron027Cobalt028Nickel029Copper030Zinc031Gallium032Germanium033Arsenic034Selenium035Bromine036Krypton037Rubidium038Strontium039Yttrium040Zirconium041Niobium042Monlbdenum043Technetium044Ruthenium045Rhodium046Palladium047Silver048Cadmium049Indium050Tin051Antimony052Tellurium053Iodine054Xenon055Caesium056Barium057Lanthanum058Cerium059Praseodymium060Neodynium061Promethium062Samarium063Europium064Gadolinium065Terbium066Dysprosium067Holmium068Erbium069Thulium070Ytterbium071Lutetium072Halfnium073Tantalum074Tungsten075Rhenium076Osmium077Iridium078Platinum079Gold080Mercury081Thallium082Lead083Bismuth084Polonium085Astatine086Radon087Francium088Radium089Actinium090Thorium091Protactinium092Uranium093Neptunium094Plutonium095Americium096Curium097Berkelium098Californium099Einsteinium100Fermium101Mendelevium102Nobelium103Lawrencium104Rutherfordium105Dubnium106Seaborgium107Bohrium108Hassium109Meitnerium110Darmstadtium111Roentgenium112Copernicium113Nihonium114Flerovium115Moscovium116Livermorium117Tennessine118Oganesson";
		int ph3=0;
		String result="";
		boolean theOne=false;
		if (ord!=118) {
			while (!(theOne)) {
				result="";
				// ((Integer.parseInt(String.valueOf(fullTable.charAt(ph3)) + String.valueOf(fullTable.charAt(ph3+1)) + String.valueOf(fullTable.charAt(ph3+2))))==ord)
				theOne=((Integer.parseInt(String.valueOf(fullTable.charAt(ph3)) + String.valueOf(fullTable.charAt(ph3+1)) + String.valueOf(fullTable.charAt(ph3+2))))==ord);
				ph3=ph3+3;
				while (!((fullTable.charAt(ph3)=='0')||(fullTable.charAt(ph3)=='1'))) {
					result=result + String.valueOf(fullTable.charAt(ph3));
					ph3=ph3+1;
				}
			}
		}else {
			result="Oganesson";
		}
		return result;
	}
	public static boolean clean(String Word) {
		int ph4=0;
		boolean answ=true;
		while ((ph4)<Word.length()) {
			if (Word.charAt(ph4)=='_') {
				answ=false;
				return answ;
			}
			ph4=ph4+1;
		}
		return answ;
	}
	public static void main(String[] args) {
		Scanner kybd = new Scanner(System.in);
		String nother="";
		while (1==1) {
			System.out.println("Enter a" + nother + " Word, and I'll break it up into Element names:");
			nother="nother";
			String WORD=kybd.nextLine();
			String keep=WORD;
			String Result="";
			String newWord="";
			String Result2="";
			String Result3="";
			int MyNumber=0;
			int ph1=1;
			boolean possible=clean(keep);
			while ((WORD.length()>1)&&possible) {
				if (((findEle(WORD.charAt(0), Long(WORD, 1))))&&((!(2<WORD.length()))||((findEle(Long(WORD, 2),'_'))||(findEle(Long(WORD, 2),Long(WORD, 3)))))) {
					ph1=0;
					while (!((String.valueOf(Character.toUpperCase(WORD.charAt(0))) + String.valueOf(Character.toUpperCase(WORD.charAt(1)))).equals((placeEleUpper(ph1))))) {
						ph1=ph1+1;
					}
					Result=Result + placeEle(ph1);
					ph1=ph1+1;
					if (keep==WORD) {
						Result2=String.valueOf(ph1);
						Result3=nameIt(ph1);
					}else {
						Result2=Result2 + ", " + String.valueOf(ph1);
						Result3=Result3 + ", " + nameIt(ph1);
					}
					MyNumber=MyNumber+ph1;
					ph1=3;
					newWord="";
					while (!(ph1>(WORD.length()))) {
						newWord=newWord+((WORD.charAt(ph1-1)));
						ph1=ph1+1;
					}
				}else if (possible&&(findEle(WORD.charAt(0), '_'))) {
					ph1=0;
					while (!((String.valueOf(Character.toUpperCase(WORD.charAt(0)))).equals((placeEleUpper(ph1))))) {
						ph1=ph1+1;
					}
					Result=Result + placeEle(ph1);
					ph1=ph1+1;
					if (keep==WORD) {
						Result2=String.valueOf(ph1);
						Result3=nameIt(ph1);
					}else {
						Result2=Result2 + ", " + String.valueOf(ph1);
						Result3=Result3 + ", " + nameIt(ph1);
					}
					MyNumber=MyNumber+ph1;
					ph1=2;
					newWord="";
					while (!(ph1>(WORD.length()))) {
						newWord=newWord+((WORD.charAt(ph1-1)));
						ph1=ph1+1;
					}
				}else {
					possible=false;
				}
				WORD=newWord;
				System.out.println(Result+"   |   "+WORD);
			}
			if ((WORD.length()==1)&&(findEle(WORD.charAt(0),'_'))) {
				ph1=0;
				while (!((String.valueOf(Character.toUpperCase(WORD.charAt(0)))).equals((placeEleUpper(ph1))))) {
					ph1=ph1+1;
				}
				Result=Result + placeEle(ph1);
				ph1=ph1+1;
				if (keep==WORD) {
					Result2=String.valueOf(ph1);
					Result3=nameIt(ph1);
				}else {
					Result2=Result2 + ", " + String.valueOf(ph1);
					Result3=Result3 + ", " + nameIt(ph1);
				}
				MyNumber=MyNumber+ph1;
				ph1=2;
				newWord="";
				while (!(ph1>(WORD.length()))) {
					newWord=newWord+((WORD.charAt(ph1-1)));
					ph1=ph1+1;
				}
			}else {
				if ((WORD.length()==1)) {
					possible=false;
				}
			}
			if (possible) {
				System.out.println("\n" + Result + "\n" + Result2 + "\n" + Result3 + "\n");
			}else {
				System.out.println("Sorry, but the word \"" + keep + "\" can't be broken into Element names!\n");
			}
		}
	}
}