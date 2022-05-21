/*
구현해야 하는 것.

input-form에서 넘어온 value 정보를 저장할 객체
todo-list에 li 삽입하는 function
logic : todo-input 에서 입력받은 문자열을 enter가 받아서(혹은 진짜 엔터) 넘긴 객체를 저장. node 추가

생각을 해보자..
parent 객체 배열에 담긴 정보가 최신화될 때마다
html을 다시 stack에 쌓아야 한다..
그럼 논리적으로 어떻게 이어져야 하는가?
stackUp() 이전에 객체 배열을 하나씩 접근하여 값을 호출하는 반복문이 선행되어야 한다.
그 반복문은 조건에 따라 또 나뉘어야 하는데, (all, remain, done)

문제점
객체를 li태그로 push하고 새로운 node를 추가할 때
기존의 push된 list를 모두 pop 해주어야 한다....

문제점...
값을 없애고 id 재설정

특정 조건에 해당하는 노드만 탐색할 때, 객체를 갱신할 것이다.
그렇다면 이 때 객체가 새로운 값에 의해 덮어씌워지게 되는데
다시 모든 노드를 화면에 띄우려면 객체를 백업해두어야 하는가???
flag를 사용하자.. 객체는 남겨두고 isComplete 값에 따라 화면에 띄울지 말지 결정한다.
*/

class Scheduler {
    constructor() {
        this.inputValue = document.querySelector(".todo-input");
        this.enterBtn = document.querySelector(".enter");
        this.todoList = document.querySelector(".todo-list");
        this.completeAllBtn = document.querySelector(".complete-all-btn");

        this.leftItem = document.querySelector(".left-items");
        this.showAll = document.querySelector(".show-all-btn");
        this.showRemain = document.querySelector(".show-remaining-btn");
        this.showDone = document.querySelector(".show-done-btn"); 
        this.clearAll = document.querySelector(".clear-all-btn");

        this.parent = [];
        this.index = 0;
    }

    set_node(newNode) { this.parent = newNode; }
    get_all_node() { return this.parent; }

    getInputValue() {
        // todo-input에 문자열을 입력받은 경우, enter을 누른 경우. 2가지 실행 방법 구현
        this.inputValue.addEventListener('keydown', (e)=>{ // e == keybord event obj
            if (e.key == "Enter")
                this.setInputValue(e.target.value);
        });
        this.enterBtn.addEventListener('click', ()=>{
            this.setInputValue(this.inputValue.value);
        });

        this.completeAllBtn.addEventListener('click', ()=>this.completeAll());
        // btn-group
        this.showAll.addEventListener('click', ()=>this.bifurcation());
        this.showRemain.addEventListener('click', ()=>this.bifurcation(1));
        this.showDone.addEventListener('click', ()=>this.bifurcation(2));
        this.clearAll.addEventListener('click', ()=>this.clearParant());
    }

    setInputValue(data) {
        if (data != "") { 
            const idx = this.index++;
            const newNode = [...this.parent, {id : idx, content : data, isComplete : false}]; // spread oper을 이용한 배열 병합
            this.set_node(newNode);

            // 블럭 쌓기 시작
            this.bifurcation();
            this.updateLeftItem();
        } else {
            alert("일정을 기입해주세요.");
        }

        this.inputValue.value = ""; // 버퍼 비우기
    }

    bifurcation(flag = 0) { // block을 쌓기 전에 어떤 노드만 쌓을 건지 분기점 체크
        this.todoList.innerHTML = null; // ul 태그 안의 모든 li 제거 (안 하면 계속 쌓인다)

        let tmp = [];
        if (flag == 0) { // all
            tmp = this.get_all_node();
            tmp.forEach(param => this.buildList(param));
        } else if (flag == 1) { // remain
            tmp = this.get_all_node().filter(param => param.isComplete == false);
            tmp.forEach(param => this.buildList(param));
        } else { // done
            tmp = this.get_all_node().filter(param => param.isComplete == true);
            tmp.forEach(param => this.buildList(param));
        }
    }

    buildList(node) {
        const block = document.createElement('li')
        block.classList.add('todo-item'); // <li class="todo-item"></li>
        
        if(node.isComplete) block.classList.add('checked');
        /*
        const inputElement = document.createElement('input');
        inputElement.classList.add('edit-input');
        */
        const checkbox_elem = document.createElement('button');
        checkbox_elem.classList.add('checkbox');
        checkbox_elem.innerHTML = "✔︎";
        checkbox_elem.addEventListener('click', ()=> this.complete(node.id));

        const content_elem = document.createElement('div');
        content_elem.classList.add('content');
        content_elem.innerHTML = node.content;
        content_elem.addEventListener('dblclick', (e)=> this.dblclick(e, node.id));

        const delete_elem = document.createElement('button');
        delete_elem.classList.add('delBtn');
        delete_elem.innerHTML = "✕";
        delete_elem.addEventListener('click', () => this.delete_node(node.id));
        
        block.appendChild(checkbox_elem);
        block.appendChild(content_elem);
        //block.appendChild(inputElement);
        block.appendChild(delete_elem);

        this.todoList.appendChild(block);
    }

    complete(nodeID) {
        // id 값을 당기면서 최신화하지 않는 이상, 인덱스 접근법은 무리가 있다.
        const newNode = this.get_all_node().map(param => (param.id == nodeID) ? {...param, isComplete : !param.isComplete} : param)
        
        this.set_node(newNode);
        this.bifurcation();
        this.updateLeftItem();
    }

    dblclick(e, nodeID) {
        const parentElement = e.target.parentElement; // 상위 태그를 가져온다.
        // create input-box
        const addAttriInput = document.createElement('input');
        addAttriInput.classList.add('edit-input'); // css 속성 사용을 위해서 클래스 추가
        addAttriInput.value = e.target.innerHTML; // 일단 기존의 내용을 가지고 있는다.

        addAttriInput.addEventListener('keydown', (e)=>{
            if (e.key == "Enter") {
                if (e.target.value != "") {
                    this.updateNode(e.target.value, nodeID);
                }
                else { alert("내용을 입력해주세요."); }
            }
        });

        parentElement.appendChild(addAttriInput);
    }

    updateNode(data, nodeID) {
        const newNode = this.get_all_node().map(param => (param.id == nodeID) ? {...param, content : data} : param)
    
        this.set_node(newNode);
        this.bifurcation();
        this.updateLeftItem();
    }

    delete_node(nodeID) {
        const newNode = this.get_all_node().filter(param => param.id != nodeID)
        this.set_node(newNode)
        this.bifurcation()
        this.updateLeftItem()
    }

    completeAll() {
        let newNode = [];

        if (this.isValid()) { // 전부 checked 되어있지 않은 경우
            this.completeAllBtn.classList.add('checked');
            newNode = this.get_all_node().map(param => {
                return param = {id : param.id, content : param.content, isComplete : true}
            })
        }
        else {
            this.completeAllBtn.classList.remove('checked');
            newNode = this.get_all_node().map(param => {
                return param = {id : param.id, content : param.content, isComplete : false}
            })
        }
        this.set_node(newNode);

        this.bifurcation();
        this.updateLeftItem();
    }

    isValid() {
        if (this.get_all_node().length != this.get_all_node().filter(param => param.isComplete == true).length)
            return true;
        return false;
    }

    clearParant() {
        const blank = []
        this.set_node(blank);
        this.bifurcation();
        this.updateLeftItem();
    }

    updateLeftItem() {
        const items = this.get_all_node().filter(param => param.isComplete == false);
        this.leftItem.innerHTML = `🤪 오늘 할 일이 ${items.length}개 남았습니다. 🤪`
    }
}