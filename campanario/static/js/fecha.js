function fechaActual() {
    let date = new Date(); 
    let yyy = date.getFullYear();
    let mmm = date.getMonth() + 1;
    let ddd = date.getDate();
    let time = yyy + "-" + mmm + "-" + ddd;
    document.getElementById("fecha").innerText = time; 
    let t = setTimeout(function(){ currentTime() }, 50000);
  }
  
  fechaActual();



