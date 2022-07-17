import styled from 'styled-components';
import NewItem from './NewsItem';
import axios from 'axios';
import usePromise from '../lib/usePromise';

const NewsListBlock = styled.div`
    box-sizing: border-box;
    padding-bottom: 3rem;
    width: 768px;
    margin: 0 auto;
    margin-top: 2rem;
    @media screen and (max-width: 768px) {
        width: 100%;
        padding-left: 1rem;
        padding-right: 1rem;
    }
`;

const NewsList = ({ category }) => {
    const [loading, response, error] = usePromise(() => {
        const query = category === 'all' ? '' : `&category=${category}`;
        return axios.get(
            `https://newsapi.org/v2/top-headlines?country=kr${query}&apiKey=a3e026cf10af4ea7bd50b254f9b39a03`,
        );
    }, [category]);

    if (loading) { return <NewsListBlock>로딩 중..</NewsListBlock>}
    if (!response) { return null;} // 이 과정을 안 넣으면 데이터가 없을 때, null에 map함수를 쓰는 상황이 벌어짐. => 렌더링 오류
    if (error) { return <NewsListBlock>에러 발생</NewsListBlock> }

    const { articles } = response.data;
    return (
        <NewsListBlock>
            {articles.map(article => (
                <NewItem key={article.url} article={article} />
            ))}
        </NewsListBlock>
    )
}

export default NewsList;