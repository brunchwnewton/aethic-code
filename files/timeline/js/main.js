var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
var mya = 0;
document.getElementById("myaWrite").value=mya;

var miracles = [
	[4500,"Alpha","α"],
	[4100,"Beta","β"],
	[3800,"Gamma","γ"],
	[2300,"Epsilon Start","ε₀"],
	[2000,"Delta","δ"],
	[1300,"Epsilon Finish","ε₁"],
	[233.23,"Zeta","ζ"],
	[66.01,"Eta","η"],//Make this 66 exactly to show up on both eras -> Precaution that there is an as yet unsolved glitch there though
	[2,"Theta","θ"],
]

var spans = [
	[0,"Hadean",4600,0],
	[0,"Archean",4000,1],
	[0,"Proterozoic",2500,1],
	[0,"Phanerozoic",541,1],
	[1,"Eoarchean",0,0],
	[1,"Paleoarchean",3600,1],
	[1,"Mesoarchean",3200,1],
	[1,"Neoarchean",2800,1],
	[1,"Paleoproterozoic",0,0],
	[1,"Mesoproterozoic",1600,1],
	[1,"Neoproterozoic",1000,1],
	[1,"Dawn",0,0],//Paleozoic
	[1,"Dark",251.902,1],//Mesozoic
	[1,"New",66,1],//Cenozoic
	[2,"Siderian",0,0],
	[2,"Rhyacian",2300,1],
	[2,"Orosirian",2050,1],
	[2,"Statherian",1800,1],
	[2,"Calymmian",0,0],
	[2,"Ectasian",1400,1],
	[2,"Stenian",1200,1],
	[2,"Tonian",0,0],
	[2,"Cryogenian",720,1],
	[2,"Ediacaran",635,1],
	[2,"Cambrian",0,0],
	[2,"Ordovician",485.4,1],
	[2,"Silurian",443.8,1],
	[2,"Devonian",419.2,1],
	[2,"Carboniferous",358.9,1],
	[2,"Permian",298.9,1],
	[2,"Triassic",0,0],
	[2,"Jurassic",201.3,1],
	[2,"Cretaceous",145,1],
	[2,"Paleogene",0,0],
	[2,"Neogene",23.03,1],
	[2,"Quaternary",2.58,1],
	[3,"Terreneuvian",0,0],
	[3,"Series 2",521,1],
	[3,"Miaolingian",509,1],
	[3,"Furongian",497,1],
	[3,"Early Ordovician",0,0],
	[3,"Middle Ordovician",470,1],
	[3,"Late Ordovician",458.4,1],
	[3,"Llandovery",0,0],
	[3,"Wenlock",433.4,1],
	[3,"Ludlow",427.4,1],
	[3,"Pridoli",423,1],
	[3,"Early Devonian",0,0],
	[3,"Middle Devonian",393.3,1],
	[3,"Late Devonian",382.7,1],
	[3,"Mississippian",0,0],
	[3,"Pennsylvanian",323.2,1],
	[3,"Cisuralian",0,0],
	[3,"Guadalupian",272.95,1],
	[3,"Lopingian",259.1,1],
	[3,"Early Triassic",0,0],
	[3,"Middle Triassic",247.2,1],
	[3,"Late Triassic",237,1],
	[3,"Early Jurassic",0,0],
	[3,"Middle Jurassic",174.1,1],
	[3,"Late Jurassic",163.5,1],
	[3,"Early Cretaceous",0,0],
	[3,"Late Cretaceous",100.5,1],
	[3,"Paleocene",0,0],
	[3,"Eocene",56,1],
	[3,"Oligocene",33.9,1],
	[3,"Miocene",0,0],
	[3,"Pliocene",16.0/3,1],
	[3,"Pleistocene",0,0],
	[3,"Holocene",0.0117,1],
	[4,"Fortunian",0,0],
	[4,"Stage 2",529,1],
	[4,"Stage 3",0,0],
	[4,"Stage 4",514,1],
	[4,"Wuliuan",0,0],
	[4,"Drumian",504.5,1],
	[4,"Guzhangian",500.5,1],
	[4,"Paibian",0,0],
	[4,"Jiangshanian",494,1],
	[4,"Stage 10",489.5,1],
	[4,"Tremadocian",0,0],
	[4,"Floian",477.7,1],
	[4,"Dapingian",0,0],
	[4,"Darriwilian",467.3,1],
	[4,"Sandbian",0,0],
	[4,"Katian",453,1],
	[4,"Hirnantian",445.2,1],
	[4,"Rhuddanian",0,0],
	[4,"Aeronian",440.8,1],
	[4,"Telychian",438.5,1],
	[4,"Sheinwoodian",0,0],
	[4,"Homerian",430.5,1],
	[4,"Gorstian",0,0],
	[4,"Ludfordian",425.6,1],
	[4,"Pridoli",0,0],
	[4,"Lochkovian",0,0],
	[4,"Pragian",410.8,1],
	[4,"Emsian",407.6,1],
	[4,"Eifelian",0,0],
	[4,"Givetian",387.7,1],
	[4,"Frasnian",0,0],
	[4,"Famennian",372.2,1],
	[4,"Tournaisian",0,0],
	[4,"Viséan",346.7,1],
	[4,"Serpukhovian",330.9,1],
	[4,"Bashkirian",0,0],
	[4,"Moscovian",315.2,1],
	[4,"Kasimovian",307,1],
	[4,"Gzhelian",303.7,1],
	[4,"Asselian",0,0],
	[4,"Sakmarian",295,1],
	[4,"Artinskian",290.1,1],
	[4,"Kungurian",283.5,1],
	[4,"Roadian",0,0],
	[4,"Wordian",268.8,1],
	[4,"Capitanian",265.1,1],
	[4,"Wuchiapingian",0,0],
	[4,"Changhsingian",254.14,1],
	[4,"Induan",0,0],
	[4,"Olenekian",251.2,1],
	[4,"Anisian",0,0],
	[4,"Ladinian",242,1],
	[4,"Carnian",0,0],
	[4,"Norian",227,1],
	[4,"Rhaetian",208.5,1],
	[4,"Hettangian",0,0],
	[4,"Sinemurian",199.3,1],
	[4,"Pliensbachian",190.8,1],
	[4,"Toarcian",182.7,1],
	[4,"Aalenian",0,0],
	[4,"Bajocian",170.3,1],
	[4,"Bathonian",168.3,1],
	[4,"Callovian",166.1,1],
	[4,"Oxfordian",0,0],
	[4,"Kimmeridgian",157.3,1],
	[4,"Tithonian",152.1,1],
	[4,"Berriasian",0,0],
	[4,"Valanginian",139.8,1],
	[4,"Hauterivian",132.9,1],
	[4,"Barremian",129.4,1],
	[4,"Aptian",125,1],
	[4,"Albian",113,1],
	[4,"Cenomanian",0,0],
	[4,"Turonian",93.9,1],
	[4,"Coniacian",89.8,1],
	[4,"Santonian",86.3,1],
	[4,"Campanian",83.6,1],
	[4,"Maastrichtian",72.1,1],
	[4,"Danian",0,0],
	[4,"Selandian",61.6,1],
	[4,"Thanetian",59.2,1],
	[4,"Ypresian",0,0],
	[4,"Lutetian",47.8,1],
	[4,"Bartonian",41.2,1],
	[4,"Priabonian",37.8,1],
	[4,"Rupelian",0,0],
	[4,"Chattian",27.8,1],
	[4,"Aquitanian",0,0],
	[4,"Burdigalian",20.44,1],
	[4,"Langhian",15.97,1],
	[4,"Serravallian",13.82,1],
	[4,"Tortonian",11.63,1],
	[4,"Messinian",7.246,1],
	[4,"Zanclean",0,0],
	[4,"Piacenzian",3.6,1],
	[4,"Gelasian",0,0],
	[4,"Calabrian",1.8,1],
	[4,"Chibanian",0.774,1],
	[4,"Late Pleistocene",0.129,1],
	[4,"Greenlandian",0.0117,1],
	[4,"Northgrippian",0.0082,1],
	[4,"Meghalayan",0.0042,1]
  ]

  var tl2Start = 0;
  var tl2End = 0;
  var tl3Start = 0;
  var tl3End = 0;
  var tl4Start = 0;
  var tl4End = 0;

  var tl2Shift = 0;
  var tl3Shift = 0;

  var cursorSelected = [false,false,false];
  var cursorDragged = false;

  document.getElementById("cursor1").onmouseover = function(){cursorSelected[0]=true};
  document.getElementById("cursor2").onmouseover = function(){cursorSelected[1]=true};
  document.getElementById("cursor3").onmouseover = function(){cursorSelected[2]=true};
  document.getElementById("cursor1").onmouseleave = function(){cursorSelected[0]=false};
  document.getElementById("cursor2").onmouseleave = function(){cursorSelected[1]=false};
  document.getElementById("cursor3").onmouseleave = function(){cursorSelected[2]=false};


var spotlight = 1;//1, 2, or 3 -> sets the spotlight timeline


// Make the DIV element draggable:
dragElement(document.getElementById("cursor1"));
dragElement(document.getElementById("cursor2"));
dragElement(document.getElementById("cursor3"));

function dragElement(elmnt) {
	cursorDragged = true;
  cursorSelected[elmnt.id.charAt(elmnt.id.length-1)-1] = true;
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
	//elmnt.style.top = (elmnt.offsetTop - pos2) + "px"; //KEEP STATIC FOR X ONLY MOTION

	var goTo = (elmnt.offsetLeft - pos1);
	if (goTo>canvas.width*0.99999) {
		goTo=canvas.width*0.99999;
	}else if (goTo<0) {
		goTo=0;
	}

	elmnt.style.left = (goTo-(0)) + "px";//IMPORTANT -> ACTUALLY SETS THE X POSITION
	
	var cursorNum = null;
	if (elmnt.id=="cursor1") {
		cursorNum=1;
	}else if (elmnt.id=="cursor2") {
		cursorNum=2;
	}else if (elmnt.id=="cursor3") {
		cursorNum=3;
	}
	cursorTo(goTo,cursorNum);
	cursorSelected[elmnt.id.charAt(elmnt.id.length-1)-1] = false;
  }

  

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
	cursorDragged = false;
  }
}

function cursorTo(goTo,cursorNum) {
	if (cursorNum==1) {
		spotlight=1;
		mya = (1-goTo*1.0/canvas.width) * 4600;
	}else if (cursorNum==2) {
		spotlight=2;
		var start = tl2Start;
		var end = tl2End;
		mya = end + (1-goTo*1.0/canvas.width) * (start-end);
	}else if (cursorNum==3) {
		spotlight=3;
		var start = tl3Start;
		var end = tl3End;
		mya = end + (1-goTo*1.0/canvas.width) * (start-end);
	}
	document.getElementById("spotlight").value = spotlight;

	document.getElementById("cursor"+cursorNum).style.left = (goTo-(0)) + "px"

	drawTimelineDynamic();
	update();
  }

  function cursorToArray(array) {
	  cursorTo(array[0],array[1]);
  }

  function miracleGetsClicked(array) {
	  isMiracleClicked = true;
	  cursorToArray(array);
  }

  function update() {
	updateMap();
	document.getElementById("momentDesc").innerHTML = getMomentDescription(mya);
	for (var i=1; i<=3; i++) {
		var elm = document.getElementById("cursor"+i);
		if (elm.id!="cursor"+spotlight) {
			var goTo;
			var start;
			var end;
			document.getElementById("myaWrite").value=Math.floor(mya);
			if (spotlight==1) {
				if (elm.id=="cursor2") {
					start = tl2Start;
					end = tl2End;
				}else if (elm.id=="cursor3") {
					start = tl3Start;
					end = tl3End;
				}
			}else if (spotlight==2) {
				if (elm.id=="cursor1") {
					start = 4600;
					end = 0;
				}else if (elm.id=="cursor3") {
					start = tl3Start;
					end = tl3End;
				}
			}else if (spotlight==3) {
				if (elm.id=="cursor2") {
					start = tl2Start;
					end = tl2End;
				}else if (elm.id=="cursor1") {
					start = 4600;
					end = 0;
				}
			}
			goTo = (start-mya)*1.0/(start-end)*canvas.width;
			elm.style.left = goTo + "px";
			if ((mya>=spans[3][2]+0.001 && i==3)||(mya>=spans[2][2]+0.001 && i==2)) {
				elm.style.visibility = "hidden";
			}else {
				elm.style.visibility = "visible";
			}
		}
	}
  }

  function updateMap() {
	var map = document.getElementById("map");
	map.currentTime = (1-(mya-1)/1000) * 40;//Total video time is 40 seconds, and the time to map this to is 1000 mya
	if (mya>1000) {
		map.style.visibility = "hidden";
	}else {
		map.style.visibility = "unset";
	}
  }

function spotlightZero() {
	mya = document.getElementById("myaWrite").value;
	document.getElementById("momentDesc").innerHTML = getMomentDescription(mya);

	drawTimelineDynamic();

	for (var i=1; i<=3; i++) {
		var elm = document.getElementById("cursor"+i);
		var goTo;
		var start;
		var end;



		if (elm.id=="cursor1") {
			start = 4600;
			end = 0;
		}else if (elm.id=="cursor2") {
			var look = lookupByMYA(mya,0);
			start = lookup(0,look);
			//document.getElementById("spotlight").value=start;
			end = lookup(0,look+1);
			if (spans[look+1][0]!=0) {
				end = 0;
			}
		}else if (elm.id=="cursor3") {
			var look = lookupByMYA(mya,1);
			start = lookup(1,look);
			//document.getElementById("spotlight").value=start;
			end = lookup(1,look+1);
			if (spans[look+1][0]!=1) {
				end = 0;
			}
		}
		goTo = (start-mya)*1.0/(start-end)*canvas.width;
		elm.style.left = goTo + "px";
		if ((mya>=spans[3][2]+0.001 && i==3)||(mya>=spans[2][2]+0.001 && i==2)) {
			elm.style.visibility = "hidden";
		}else {
			elm.style.visibility = "visible";
		}
	}
	
	updateMap();
}

class sound {
	constructor(src) {
		this.sound = document.createElement("audio");
		this.sound.src = src;
		this.sound.setAttribute("preload", "auto");
		this.sound.setAttribute("controls", "none");
		this.sound.style.display = "none";
		document.body.appendChild(this.sound);
		this.play = function () {
			this.sound.play();
		};
		this.stop = function () {
			this.sound.pause();
		};
	}
}


























  function upZero(group,openCount,spans) {
	var addend = 0;
	if (group==0) {
		addend = 0;
	}else if (group==1) {
		addend = 1;
	}else if (group==2) {
		addend = 4;
	}else if (group==3) {
		addend = 10;
	}

	var index=0;
	for (index=0; spans[index][0]<group-1; index++);
	for (var ind=0;ind<openCount;ind++){
		index++;
	}
	index+=addend;
	if (spans[index][3]==0) {
		var openCount2=0;
		var index2=0;
		for (index2=0; index2<index; index2++) {
			if (spans[index2][0]==group-1 && spans[index2][3]==0) {
				openCount2++;
			}
		}
		/*if (spans[index2][1]=="Siderian") {
			ctx.fillStyle = 'black';
			ctx.font = "30px Arial";
			ctx.fillText(""+openCount2,0,300);
		}*/
		if (group>0) {
			return upZero(group-1,openCount2,spans);
		}
	}
	return spans[index][2];
  }

  function lookup(group,count) {
	if (count==0) {
		return spans[0][2];
	}
	var i=group;
	var stage = spans[count];
	var stageStart = stage[2];
	if (stage[0]==i) {
		if (stage[3]==0) {
			var openCount=0;
			for (index2=0; index2<count; index2++) {
				if (spans[index2][0]==i && spans[index2][3]==0) {
					openCount++;
				}
			}
			stageStart = upZero(i,openCount,spans);
		}
	}else {
		return 0;
	}
	return stageStart;
  }

  function myaToTimeline(mya,start,end,totalLength) {
	var place = (start-mya)/(start-end);
	return parseInt(Math.round(totalLength*(place)));
  }

  function jumpUp(count) {
	  var stage = spans[count];
	  var group = stage[0];
	  if (group==0) {
		  return -1;
	  }
	  for (var i=0; spans[i][0]<=group-1; i++) {
		var front = spans[i];
		var back = spans[i+1];

		if (spans[i][0]==group-1 && back[0]!=group-1) {
			return i;
		}

		if (stage[2]<=lookup(group,i) && stage[2]>lookup(group,i+1)) {
			return i;
		}
	  }
	  return -2;
  }

  function lookupByMYA(mya,group) {
	  if (mya>spans[1][2]) {
		  return 0;
	  }
	  for (var i=0; i<spans.length; i++) {
		  if (i+1>=spans.length) {
			  return i;
		  }else if (spans[i][0]==group) {
			  if (spans[i+1][0]!=group) {
				  return i;
			  }
			  if (lookup(group,i)>=mya && lookup(group,i+1)<mya) {
				  return i;
			  }
		  }
	  }
	  return -2;
  }

  function scaleToFill(img,width,height,xPlace,yPlace){
    // get the scale
    var scale = Math.max(width / img.width, height / img.height);
    // get the top left position of the image
    var x = (width / 2) - (img.width / 2) * scale;
    var y = (height / 2) - (img.height / 2) * scale;
    ctx.drawImage(img, x+xPlace, y+yPlace, img.width * scale, img.height * scale);
}

function drawMiracles(yHeight,stageStart,stageEnd) {
	drawMiraclesStatic(yHeight,stageStart,stageEnd);
}
function drawMiraclesStatic(yHeight,stageStart,stageEnd) {
	for (var i=0; i<miracles.length; i++) {
		
	}
}

  function drawTimeline() {
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	var totalLength = canvas.width;
	var totalHeight = totalLength/24;
  
	var count=0;
	var countSave=0;
  
	for (var i=0; i<3; i++) {//FIX TO 3 IF FAIL!
		var yStartSave=0;
		var startSave=0;
		var endSave=0;

		var upStart = 4600;
		var upEnd = 0;
		if (i>=1) {
			var groupLookup = i-1;
			if (groupLookup<0) {
				groupLookup=0;
			}
			var up = lookupByMYA(mya,groupLookup);
			upStart = lookup(groupLookup,up);
			if (up+1<spans.length || spans[up+1][0]==spans[up][0]) {
				upEnd = lookup(groupLookup,up+1);
			}
		}

		if (i==1) {
			if (tl2Start!=upStart) {
				tl2Shift++;
			}
			tl2Start=upStart;
			tl2End=upEnd;
		} else if (i==2) {
		  if (tl3Start!=upStart) {
			  tl3Shift++;
		  }
		  tl3Start=upStart;
		  tl3End=upEnd;
		}else if (i==3) {
		  tl4Start=upStart;
		  tl4End=upEnd;
		}


		for (var k=0; k<2; k++) {
			if (k==1) {
				countSave=count;
			}else {
				count = countSave;
			}

			if ((mya>4000 && i>=1) || (mya>2500 && i>=2)) {
				return;
			}

			var group = i+k;
			for (var j=0; spans[count][0]==group; count++) {
			  var stage = spans[count];
			  var stageStart = lookup(group,count);
			  var stageEnd = lookup(group,count+1);
  
  
			  
	  
			  var yBredth = totalHeight;
			  var yStart = yBredth*i*3 + yBredth*k;
			  var xStart = myaToTimeline(stageStart,upStart,upEnd,totalLength);
			  var xEnd = myaToTimeline(stageEnd,upStart,upEnd,totalLength);
			  if (k==0) {
				  yStartSave=yStart;
				  startSave=upStart;
				  endSave=upEnd;
			  }
	  
			 if (group%2==0) {
				ctx.fillStyle = "#01010f";
				if (count%2==0) {
					ctx.fillStyle = '#0f0f1f';
				}
			 }else {
				ctx.fillStyle = '#0f0101';
				if (count%2==0) {
					ctx.fillStyle = '#1f0f0f';
				}
			 }
  
			 ctx.fillRect(xStart,yStart,xEnd-xStart,yBredth);
  
  
			  ctx.fillStyle = 'orange';
			  ctx.font = "20px Arial";
			  ctx.fillText(stage[1],xStart,yBredth+yStart);
	  
			  j++;
			}
		}
		
		drawMiracles(yStart-totalHeight,startSave,endSave);
	}
  }

  var tl1isSet = false;
  var renderOnce = false;

  var isTransfer2;
  var isTransfer3;


  function drawTimelineDynamic() {
	//document.createElement();

	var totalLength = canvas.width;
	var totalHeight = totalLength/24;
  
	var count=0;
	var countSave=0;
  
	for (var i=0; i<3; i++) {
		var yStartSave=0;
		var startSave=0;
		var endSave=0;

		isTransfer2=false;
		isTransfer3 = false;
		var upStart = 4600;
		var upEnd = 0;
		if (i>=1) {
			tl1isSet=true;
			var groupLookup = i-1;
			if (groupLookup<0) {
				groupLookup=0;
			}
			var up = lookupByMYA(mya,groupLookup);
			upStart = lookup(groupLookup,up);
			if (up+1<spans.length || spans[up+1][0]==spans[up][0]) {
				upEnd = lookup(groupLookup,up+1);
			}
		}

		if (i==1) {
			if (tl2Start!=upStart) {
				tl2Shift++;
				isTransfer2 = true;
				isTransfer3 = true;
			}
			tl2Start=upStart;
			tl2End=upEnd;
		} else if (i==2) {
		  if (tl3Start!=upStart) {
			  tl3Shift++;
			  isTransfer3 = true;
		  }
		  tl3Start=upStart;
		  tl3End=upEnd;
		}else if (i==3) {
		  tl4Start=upStart;
		  tl4End=upEnd;
		}

		for (var k=0; k<2; k++) {
			if (k==1) {
				countSave=count;
			}else {
				count = countSave;
			}

			var group = i+k;
			for (var j=0; spans[count][0]==group; count++) {
			  var stage = spans[count];
			  var stageStart = lookup(group,count);
			  var stageEnd = lookup(group,count+1);

			  

			
			  var goAhead = false;//goAhead tells us if we're free to create the element, based on possibility + newness
	  
			  var yBredth = totalHeight;
			  var yStart = yBredth*i*3 + yBredth*k;
			  var xStart = myaToTimeline(stageStart,upStart,upEnd,totalLength);
			  var xEnd = myaToTimeline(stageEnd,upStart,upEnd,totalLength);
			  if (k==0) {
				  yStartSave=yStart;
				  startSave=upStart;
				  endSave=upEnd;
			  }
			  
			  var myColor='white';

			 if (group%2==0) {
				myColor = "#01010f";
				if (count%2==0) {
					myColor = '#0f0f1f';
				}
			 }else {
				myColor = '#0f0101';
				if (count%2==0) {
					myColor = '#1f0f0f';
				}
			 }
  


			 //IT ALL STARTS HERE -> PRINTING
			 var spanTitle = "Span_"+i+"_"+stage[1];
			 if (i==0) {
				if (!tl1isSet) {
					goAhead = true;
				}
				
			 } else if (i==1) {
			   if (isTransfer2) {
				if (upStart>=stageStart && upEnd<=stageEnd && upStart<=spans[2][2]) {// GENERATE
					goAhead = true;
				}else {// REMOVE
					try {
						var elem = document.getElementById(spanTitle);
						elem.parentNode.removeChild(elem);
					} catch (error) {}
					
				}
			   }else {
				   
			   }
			 }else if (i==2) {
				if (isTransfer3) {
					if (upStart>spans[1][2]) {
						upEnd = spans[1][2];
					}
					if (upStart>=stageStart && upEnd<=stageEnd && upStart<=spans[3][2]) {// GENERATE
						goAhead = true;
					}else {// REMOVE
						try {
							var elem = document.getElementById(spanTitle);
							elem.parentNode.removeChild(elem);
						} catch (error) {}
						
					}
				}else {
					   
				}
			 }

			 if (goAhead) {
				var elem = document.createElement("BUTTON");
				elem.id = spanTitle;
				elem.innerHTML = stage[1];
				elem.name = stage[1];
				elem.classList.add('Span');

				elem.style.left = xStart+"px";
				elem.style.top = (yBredth*k)+"px";
				elem.style.width = (xEnd-xStart)+"px";
				elem.style.height = yBredth+"px";

				elem.style.background = myColor;

				var saveColor = myColor;
				elem["colorSave"] = myColor;
				//Object.assign(saveColor,myColor);

				document.getElementById("timeline"+(i+1)).appendChild(elem);//VERY IMPORTANT -> THIS IS WHERE THE CODE ACTUALLY INPUTS THE SPAN

				var titleSave = spanTitle+"";
				elem["partner"] = null;
				try {
					if (i>0 || (i==0 && k==1)) {
						if (k==0) {
							elem.partner = document.getElementById("Span_"+(i-1)+"_"+stage[1]);
						}else {
							elem.partner = document.getElementById("Span_"+(i+1)+"_"+stage[1]);
						}
						elem.partner.partner = elem;
					}
				}catch (error) {
					elem.partner = null;
				}
				
				var runThrough = [elem];
				elem.onmouseover = ( function(n){ return function(){mouseOver(n);} } )( runThrough );
				elem.onmouseout = ( function(n){ return function(){mouseOut(n);} } )( runThrough );
				
				function mouseOver(through) {
					var me = through[0];
					var title = me.id;
					me.style.background = "rgb(64,0,0)";

					var partnerColor = "rgb(158,47,0)";
					me.partner.style.background = partnerColor;
					try {
						//through[2].style.background = "orange";
					} catch (error) {

					}
				}
				
				function mouseOut(through) {
					var me = through[0];
					var title = me.id;
					var color = me.colorSave;
					me.style.background = color;

					me.partner.style.background = me.partner.colorSave;

					try {
						//through[2].style.background = through[2].colorSave;
					} catch (error) {
						
					}
				}
				
				
			 }

			 /*//ctx.fillRect(xStart,yStart,xEnd-xStart,yBredth);
  
  
			  ctx.fillStyle = 'orange';
			  ctx.font = "20px Arial";
			  ctx.fillText(stage[1],xStart,yBredth+yStart);*/
	  
			  j++;
			}
		}
		
		//drawMiracles(yStart-totalHeight,startSave,endSave);
		drawMiraclesDynamic(0,upStart,upEnd,i);
	}
	
	renderOnce = true;
  }

  
			
			
  
  var isMiracleClicked = false;
  const holySound = generateHolySound();

  function drawMiraclesDynamic(yHeight,stageStart,stageEnd,ord) {
	  for (var i=0; i<miracles.length; i++) {
		  var miracle = miracles[i];
		  var textSub = miracle[2];
		  var textSuper = miracle[1];
		  var myaSet = miracle[0];
		  var goTo = (stageStart-myaSet)*1.0/(stageStart-stageEnd)*canvas.width;
		  var width=2.5;
		  var height = 150;

		  var id = "Mir_"+ord+"_"+textSuper;

		  var goAhead = false;
		  var isIn = goTo>=0 && goTo<=canvas.width;
		  if (ord==0) {
			if (!tl1isSet) {
				goAhead = true;
			}
		 } else if (ord==1) {
		   if (isTransfer2) {
			if (isIn && myaSet<=spans[2][2]) {// GENERATE
				goAhead = true;
			}else {// REMOVE
				try {
					var elem = document.getElementById(id);
					elem.parentNode.removeChild(elem);
				} catch (error) {}
				
			}
		   }else {
			   
		   }
		 }else if (ord==2) {
			if (isTransfer3) {
				if (isIn && myaSet<=spans[3][2]) {// GENERATE
					goAhead = true;
				}else {// REMOVE
					try {
						var elem = document.getElementById(id);
						elem.parentNode.removeChild(elem);
					} catch (error) {}
					
				}
			   }else {
				   
			   }
		 }

		  if (goAhead) {
			var elem = document.createElement("DIV");
			elem.id = id;
			//elem.innerHTML = textSub;
			elem.name = textSuper+" Miracle";
			elem.classList.add('Miracle');
  
			elem.style.left = (goTo-width/2)+"px";
			elem.style.top = yHeight+"px";
			elem.style.width = width+"px";
			elem.style.height = height+"px";
			elem.style.position = "absolute";
  
			var myColor = 'silver';
			elem.style.background = myColor;
  
			var saveColor = myColor;
			elem["colorSave"] = myColor;
  
			//ctx.fillText(text,goTo-6,yHeight+height+18);
  
			document.getElementById("timeline"+(ord+1)).appendChild(elem);

			var label = document.createElement("LABEL");
			label.innerHTML = textSub;
			label.classList.add('MiraLabel');

			label.style.position = "absolute";
			label.style.top = height+"px";
			label.style.left = (-3) + "px";

			elem.appendChild(label);
			elem["label"] = label;

			elem["friends"] = [];
			for (var j=0; j<=ord; j++) {
				var friend;
				try {
					friend = document.getElementById("Mir_"+(j)+"_"+textSuper);
					elem.friends.push(friend);
					if (j<ord) {
						friend.friends.push(elem);
					}
				}catch (error) {
					//friends.push(null);//In case it isn't visible or something
				}
			}

			var runThrough = [elem, holySound];
			elem.onmouseover = ( function(n){ return function(){mouseOver(n);} } )( runThrough );
			elem.onmouseout = ( function(n){ return function(){mouseOut(n);} } )( runThrough );
			elem.onclick = ( function(n){ return function(){miracleGetsClicked(n);} } )( [goTo,ord+1] );

			function mouseOver(through) {
				if (!false) {
					through[1].play();
				}
				var group = through[0].friends;
				for (var j=0; j<group.length; j++) {
					var me = group[j];
					var title = me.id;
					document.getElementById(title).style.background = "gold";
					me.label.style.color = "gold";
				}
				try {
					//through[2].style.background = "orange";
				} catch (error) {

				}
				
				//var audio = new Audio('../audio/HolySound.wav');
				//audio.play();
			}
			
			function mouseOut(through) {
				if (!isMiracleClicked) {
					through[1].pause();

					if (through[1].currentTime>1.75) {
						through[1].currentTime = 0;
					}

				}
				isMiracleClicked = false;

				var group = through[0].friends;
				for (var j=0; j<group.length; j++) {
					var me = group[j];
					var title = me.id;
					var color = me.colorSave;
					document.getElementById(title).style.background = color;
					me.label.style.color = color;
				}
				try {
					//through[2].style.background = through[2].colorSave;
				} catch (error) {
					
				}

				
			}
		  }
	  }
  }

  function generateWavSound(link) {
	var holySound = document.createElement("audio");
	var holySoundSource = document.createElement("source");
	holySoundSource.src = link;
	holySoundSource.type = "audio/wav";
	holySound.appendChild(holySoundSource);
	return holySound;
  }

  function generateHolySound() {
	return generateWavSound("audio/HolySound.wav");
  }