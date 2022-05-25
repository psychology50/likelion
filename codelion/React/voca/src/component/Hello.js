/*
const Hello = function() {
    <p>Hello</p>;
}
export default Hello;
*/

import World from "./World";

/*
const Hello = () => {
    <p>Hello</p>;
}

export default Hello;
*/

import styles from "./Hello.module.css";

export default function Hello() {
    return (
        <div>
            <h1 style= {
                {
                    color : "#f00",
                    borderRight : '2px solid $000',
                    marginBottom : '30px',
                    opacity : 0.5
                }
            }>Hello</h1>
            <div className={styles.box}>Hello</div>
            <World age={10}/>
            <World age={20}/>
            <World age={30}/>
        </div>
    ); // div로 감싸지 않으면 에러가 난다. JSX는 하나의 태그만 return 할 수 있음
}