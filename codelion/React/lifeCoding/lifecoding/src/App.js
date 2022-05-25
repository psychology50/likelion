import logo from './logo.svg';
import './App.css';
import {useState} from 'react' // 훅을 이용한 state 만들기

function Header(props) {
  return (
    <header>
        <h1><a href="/" onClick={(e) => {
          e.preventDefault(); // a 태그의 기본 기능을 막는다
          props.onChangeMode();
        }}>{props.title}</a></h1>
      </header>
  );
}

function Nav(props) {
  const lis = []
  for (let i=0; i<props.topics.length; i++) {
    let t = props.topics[i];
    lis.push(<li key={t.id}>
        <a id={t.id} href={'/read' + t.id} onClick={(e)=>{
          e.preventDefault();
          props.onChangeMode(Number(e.target.id));
        }}>{t.title}</a>
      </li>)
  }
  return (
    <nav>
        <ol>
          {lis}
        </ol>
      </nav>
  );
}

function Article(props) {
  return (
    <article>
        <h2>{props.title}</h2>
        {props.body}
      </article>
  );
}

function Create(props) {
  return (
    <article>
      <h2>Create</h2>
      <form onSubmit={(e) => { // form 태그는 submit을 했을 때, 페이지가 reload 된다.
        e.preventDefault();
        const title = e.target.title.value;
        const body = e.target.body.value;
        props.onCreate(title, body);
      }}>
        <p><input type="text" name="title" placeholder="title" /></p>
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit" value="Creat"></input></p>
      </form>
    </article>
  );
}

function Update(props) {
  const [title, setTitle] = useState(props.title);
  const [body, setBody] = useState(props.body);
  return (
    <article>
      <h2>Update</h2>
      <form onSubmit={(e) => { // form 태그는 submit을 했을 때, 페이지가 reload 된다.
        e.preventDefault();
        const title = e.target.title.value;
        const body = e.target.body.value;
        props.onUpdate(title, body);
      }}>
        <p><input type="text" name="title" placeholder="title" value={title} onChange={(e)=>{
          setTitle(e.target.value); 
        }}/></p>
        <p><textarea name="body" placeholder="body" value={body} onChange={(e)=>{
          setBody(e.target.value);
        }}></textarea></p>
        <p><input type="submit" value="Update"></input></p>
      </form>
    </article>
  );
}

function App() {
  //const _mode = useState('WELCOME');
  /*
  console.log(mode)
    ['WELCOME', f]  // 배열 리턴 
    0: "WELCOME"    // 상태의 값
    1: f()          // 상태의 값을 변경할 때 사용하는 함수
    length: 2
  */
  const [mode, setMode] = useState('WELCOME');
  // const _mode = useState('WELCOME');
  // const mode = _mode[0];
  // const setMode = _mode[1]; 와 동일한 기능을 한다
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);

  const [topics, setTopics] = useState([
    {id: 1, title: 'html', body: 'html is ...'},
    {id: 2, title: 'css', body: 'css is ...'},
    {id: 3, title: 'js', body: 'javascript is ...'},
  ])

  let content = null;
  let contextControl = null; 

  if (mode == 'WELCOME') {
    content = <Article title="Welcome" body="Hello, WEB"/>
  } else if (mode == 'READ') {
    let title, body = null;
    for (let i=0; i < topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title;
        body = topics[i].body;
      }
    } 
    content = <Article title={title} body={body}/>
    contextControl= <li><a href={'/update/' + id} onClick={(e)=>{
      e.preventDefault();
      setMode('UPDATE');
    }}>Update</a></li> 
  } else if (mode == 'CREATE') {
    content = <Create onCreate={(_title, _body)=> {
      const newTopic = {id:nextId, title:_title, body:_body}
      
      const newTopics = [...topics, newTopic]
      setTopics(newTopics)
      /*
      const[value, setValue] = useState(PRIMITIVE);
      => setValue()로 값을 지정하면 된다.

      const[value, setValue] = useState(Object);
      => spread operator 이용
      */
     setMode('READ');
     setId(nextId);
     setNextId(nextId + 1);
    }} />;
  } else if (mode === 'UPDATE') {
    let title, body = null;
    for (let i=0; i < topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title;
        body = topics[i].body;
      }
    }

    content = <Update title={title} body={body} onUpdate={(title, body) => {
      const newTopics = topics.map(x => (x.id == id) ? {...x, title:title, body:body} : x)
      setTopics(newTopics);
      setMode('READ');  
    }}/>
  }
  
  return ( // 중괄호로 감싸야 문자열이 아니라, 객체가 그대로 넘어간다.
    <div>
      <Header title="React" onChangeMode={() => {
        setMode('WELCOME');
        }}
      />
      <Nav topics={topics} onChangeMode={(_id)=>{
        setMode('READ');
        setId(_id);
        }}
      />
      {content}

      <ul>
        <li>
          <a href="/create" onClick={(e)=>{
            e.preventDefault();
            setMode('CREATE');
          }}>Create</a>
        </li>
        {contextControl}
      </ul>
    </div>

  );
}

export default App;
