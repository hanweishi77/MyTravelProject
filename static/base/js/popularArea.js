//轮播图区的ul li
const ul = document.querySelector('#popular_list')
const lis = document.querySelectorAll('#popular_list>li')
//console.log('li的个数：'+ lis.length)
//页码小框框的容器ul
const container = document.querySelector('#popular_carousel_box .popular_pagination ul')

//根据轮播图区的li个数设定轮播图容器的总宽度
ul.style.width = `${ (lis.length+1) * 330}px`
//添加页码小框的个数,li个数除以3，向上取整数
let pagesNum = Math.ceil(lis.length/3)
//生成页码小框的个数
for(let i=0;i<pagesNum;i++){
    container.innerHTML+=`<li>${i+1}</li>`
}
//1.1获取页码小框框    伪数组
const myPages = document.querySelectorAll('#popular_carousel_box .popular_pagination ul li')
//console.log(myPages.length)
myPages[0].classList.add('active')
//1.2为所有的页码小框框注册事件
for(let i=0;i<pagesNum;i++){
    myPages[i].addEventListener('click', function changeIconColor(){
        //清除所有页码小框框的背景色
        for(let j=0;j<pagesNum;j++){
            myPages[j].classList.remove('active')
        }
        //定位页码
        myPages[i].classList.add('active')
        let it =  i * (-990)
        ul.style.marginLeft = it + 'px'
    })
}