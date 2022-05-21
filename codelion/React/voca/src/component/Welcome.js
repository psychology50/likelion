export default function Welcome() {

    function showName() {
        console.log("Mike");
    }
    function showText(e) {
        console.log(e.target.value);
    }

    return (
    <div>
        <h2>Welcome</h2>
        <button onClick={showName}>Show name</button>
        <button onClick={() => console.log(30)}>Show age</button>
        <input type="text" onChange={showText} />
    </div>
    );
}