import React from "react";

const Posts = (props) => {
    const { posts } = props;
    if (!posts || posts.length === 0) return <p>Can not find any posts, sorry</p>
    return (
        <div className='container grid'>
            {posts.map((post) => {
                return (
                    <div key={post.id}>
                        {post.title.substr(0, 50)}
                        <div>
                            {post.excerpt.substr(0, 60)}
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

export default Posts;