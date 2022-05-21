import { useState } from "react";
import UserName from "./UserName";

export default function World(props) { // props는 억지로 바꾸면 안 된다. 읽기 전용이기 때문
    //let name = "Mike";
    const [name, setName] = useState('Mike');
    const [age, setAge] = useState(props.age);  
    const msg = age > 19 ? "성인입니다." : "미성년자입니다.";

    function changeName() {
        const newName = name === "Mike" ? "Jane" : "Mike";
        setName(newName);
        setAge(age + 1)
    }

    return (
        <div> 
            <h1 id="name">
                {name}({age}) : {msg}
            </h1>
            <UserName name={name}/>
            <button onClick={changeName}>Change</button>
        </div>
    );
}