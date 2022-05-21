const clock = document.querySelector(".todo-title");

const getTime = () => {
    const time = new Date();
    const hour = time.getHours();
    const min = time.getMinutes();
    const sec = time.getSeconds();

    clock.innerHTML = `${hour<10 ? `0${hour}` : hour}:${min<10 ? `0${min}` : min}:${sec<10 ? `0${sec}` : sec}`
}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init()