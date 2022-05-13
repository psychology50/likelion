const topBtn= document.querySelector("#top");
const bottomBtn= document.querySelector("#bottom");
const dressBtn= document.querySelector("#dress");
const allBtn= document.querySelector("#all");

const products=[	
    {"name":"반팔티","price":"10000"},
	{"name":"린넨 셔츠","price":"45000"},
    {"name":"긴팔티","price":"11000"},
    {"name":"린넨 바지","price":"25000"},
    {"name":"슬랙스","price":"18000"},
    {"name":"롱 원피스","price":"40000"},
    {"name":"린넨 원피스","price":"30000"}
]

// Question 1.

topBtn.addEventListener('click', ()=>call_list(0, 3));
bottomBtn.addEventListener('click', ()=>call_list(3, 5));
dressBtn.addEventListener('click', ()=>call_list(5, 7));
allBtn.addEventListener('click', ()=>call_list(0, 7));

function call_list(start, end) {
    for (let i=start; i < end; i++) {
        console.log(products[i]["name"]);
    }
}

// Question 2.

function total(parm1, parm2) {
    price1 = parseInt(products[parm1]["price"])
    price2 = parseInt(products[parm2]["price"])
    console.log(price1 + price2);
}

// Question 3.

function total(...args) {  // args 라는 배열로 인자를 받음
    let result = 0
    for (let i of args)
        result += parseInt(products[i]["price"]);
    console.log(result);
} 