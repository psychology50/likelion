import { useCallback, useState } from 'react';
import { MdAdd } from 'react-icons/md';
import './scss/TodoInsert.scss';

const TodoInsert = ({ onInsert }) => {
    const [value, setValue] = useState('');
    
    const onChange = useCallback(e => {
        setValue(e.target.value);
    }, []);

    // onClick 이벤트와 달리 onSubmit은 엔터키도 반응한다.
    const onSubmit = useCallback( // onSubmit 함수는 새로고침되는 위험성이 있다.
        e => {
            onInsert(value);
            setValue('');
            e.preventDefault(); // 새로고침 방지
        }, [onInsert, value]);

    return (
        <form className='TodoInsert' onSubmit={onSubmit}>
            <input 
                placeholder='할 일을 입력하세요' 
                value={value}
                onChange={onChange}/>
            <button type="submit">
                <MdAdd/>
            </button>
        </form>
    )
}

export default TodoInsert;