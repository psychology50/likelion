import React, { useEffect, useState } from "react";
import Posts from './Posts';
import PostLoadingComponent from './PostLoading';


export default function Content() {
    const PostLoading = PostLoadingComponent(Posts);
    const [appState, setAppState] = useState({
        loading: false, // 데이터를 수집하는 동안, loading이 화면에 출력됨
        posts: null, // API에서 반환하는 모든 데이터 저장
    })

    useEffect(() => {
        setAppState({ loading: true });
        const apiUrl = `http://127.0.0.1:8000/api/`;
        fetch(apiUrl)
            .then((data) => data.json())
            .then((posts) => {
                setAppState({ loading: false, posts: posts });
            });
    }, [setAppState]);

    return (
        <div className="App">
            <h1>Latest Posts</h1>
            <PostLoading isLoading={appState.loading} posts={appState.posts} />
        </div>
    )
}


