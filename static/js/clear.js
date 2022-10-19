const timeleft = document.querySelector('#time-left');
//console.log(timeleft)
const token = document.querySelector('#token');
//console.log(token)

const time = document.querySelector('#time');
console.log(time.textContent)

const orderDate = Date.parse(time.textContent)
//console.log(orderDate)

const myCountdown = setInterval(()=>{
const now = new Date().getTime()
//console.log(now)

const diff = orderDate - now
//console.log(diff)

const d = Math.floor(orderDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24) ))
//console.log(d)
const h = Math.floor((orderDate / (1000 * 60 * 60 ) - (now / (1000 * 60 * 60 )) ) % 24)
//console.log(h)
const m = Math.floor((orderDate / (1000 * 60 * 60 ) - (now / (1000 * 60 * 60 )) ) % 60)
//console.log(m)
const s = Math.floor((orderDate / (1000) - (now / (1000 )) ) % 60)
console.log(s)

if (diff>0){
  timeleft.innerHTML = d + 'days,'  + h + 'hours,' + m + 'minutes,'  + s + 'seconds'

}else{
  clearInterval(myCountdown)
  timeleft.innerHTML = 'order delivered please get in touch if you have any queries'

}

},1000)








//const counter = document.querySelector('#countdown-box');
  //console.log(counter)
