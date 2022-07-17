import { useParams } from 'react-router-dom';

const data = {
    user1: {
        name: "사용자1",
        description: "지나가던 사람",
    },
    user2: {
        name: "사용자2",
        description: "피곤한 사람",
    },
};

const Profile = () => {
    const params = useParams();
    const profile = data[params.username];
    
    return (
        <div>
            <h1>사용자 프로필</h1>
            {profile ? (
                <div>
                    <h2>{profile.name}</h2>
                    <p>{profile.description}</p>
                </div>
            ) : (
                <p>존재하지 않는 프로필입니다.</p>
            )}
        </div>
    );
};

export default Profile;