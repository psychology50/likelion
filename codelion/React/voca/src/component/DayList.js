//import dummy from "../db/data.json";
// import { useEffect, useState } from 'react';
import {Link} from 'react-router-dom';
import useFetch from '../hooks/useFetch';

export default function DayList() {
    const days = useFetch("http://localhost:3001/days");
    // const [days, setDays] = useState([]);

    // useEffect(()=>{
    //     fetch('http://localhost:3001/days')
    //         .then(
    //             res => {
    //             return res.json();
    //         })
    //         .then(data => {
    //             setDays(data);
    //     });
    // }, []); // count가 변경되는 경우에만 함수가 실행된다. == 의존성 배열
    // 렌더링 이후 딱 한 번만 시행되는 함수는 빈 배열을 전달하면 된다.

    return (
        <>
        <ul className="list_day">
            {days.map(day => (
                <li key={day.id}>
                    <Link to={`/day/${day.day}`}>Day {day.day}</Link>
                </li>
            ))}
        </ul>
        </>
    );
}