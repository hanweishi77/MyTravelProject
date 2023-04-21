//首页随机轮播图
// 1.初始数据
const sliderData = [
    {url:"../../../static/base/img/1.jpg", title: "欢迎来到一起旅行，快来加入我们吧"},
    {url:"../../../static/base/img/2.jpg", title: "范围覆盖，从海南到东北，伴你走过天南地北"},
    {url:"../../../static/base/img/3.jpg", title: "海量数据，分享最实用的旅游攻略，结交爱旅游的朋友"},
    {url:"../../../static/base/img/4.jpg", title: "提供最全的景区介绍、最优的旅游路线、最好的旅游服务 "}
]

//2.获取元素,接着修改图片路径,修改p里面的文字内容,修改小圆点
const img = document.querySelector("#banner .slider-wrapper img")
const p = document.querySelector("#banner .slider-footer p")
let i =0
const func_next = function(){
    i++
    if(i>=sliderData.length){
        i=0
    }
    img.src = sliderData[i].url
    p.innerHTML = sliderData[i].title
    document.querySelector("#banner .slider-indicator li.active").classList.remove('active')
    document.querySelector(`#banner .slider-indicator li:nth-child(${i + 1})`).classList.add('active')
}
const func_prev = function(){
    i--
    if(i<0){
        i= sliderData.length-1
    }
    img.src = sliderData[i].url
    p.innerHTML = sliderData[i].title
    document.querySelector("#banner .slider-indicator li.active").classList.remove('active')
    document.querySelector(`#banner .slider-indicator li:nth-child(${i + 1})`).classList.add('active')
}

//按钮业务
const next = document.querySelector("#display-btn-right")
console.log(next)
next.addEventListener('click', function (){
    func_next()
    }
)
const prev = document.querySelector("#display-btn-left")
console.log(prev)
prev.addEventListener('click', function (){
    func_prev()
    }
)

//自动播放
let timerId=setInterval(function (){
    func_next()
},4000)
//鼠标进入离开事件  阻止开启自动播放
const slider = document.querySelector("#banner")
slider.addEventListener('mouseenter', function (){
    clearInterval(timerId)
})

slider.addEventListener('mouseleave', function (){
    clearInterval(timerId)
    timerId=setInterval(function (){
        func_next()
    },4000)
})
