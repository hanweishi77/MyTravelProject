let eprev = document.querySelector('#prev')
let enext = document.querySelector('#next')
let imglist = document.querySelector('#imglist')
let left = 0
let timer
console.log(eprev)
console.log(enext)
// 滚动函数
function run(){
    if(left > 2400){
        left = 0
    }
    imglist.style.marginLeft = -left + 'px'
    timer=setTimeout(run,4000)
    left = left + 1200
}

// 图片定位函数
function img_number(x){
    let it = x * (-1200)
    imglist.style.marginLeft = it + 'px'
    left = -it

}
eprev.addEventListener("click",function (){
    let prevgo = Math.floor(left/1200)-1
    if(prevgo == -1){
        prevgo=0
    }
    img_number(prevgo)
})
enext.addEventListener("click",function (){
    let prevgo = Math.floor(left/1200)+1
    if(prevgo == 3){
        prevgo=2
    }
    img_number(prevgo)
})

imglist.addEventListener('mouseenter',function (){
    clearTimeout(timer)
})
imglist.addEventListener('mouseleave', function (){
    timer = setTimeout(run, 4000)
})
