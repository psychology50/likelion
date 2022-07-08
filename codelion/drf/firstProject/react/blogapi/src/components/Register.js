import React, { useState } from "react";
import axiosInstance from '../axios';
import { useHistory } from 'react-router-dom'

export default function SignUp() {
    const history = useHistory();
    const initialFormData = Object.freeze({ // freeze: email, username, password를 입력하게 한다. 
        email: '',                          // 한 번 커밋하면 특정 방식으로 변경할 수 없도록 정보를 동결시킨다. (보안)
        username: '',
        password: '',
    })

    const [formData, updateFormData] = useState(initialFormData);

    const handleChange = (e) => {
        updateFormData({
            ...formData,
            //Trimming any whitespace
            [e.target.name]: e.target.value.trim(),
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);

        axiousInstance
            .post(`user/register/`, {
                email: formData.email,
                user_name: formData.username,
                password: formData.password,
            })
            .then((res) => {
                history.push(`/login`);
                console.log(res);
                console.log(res.data);
            });
    };

    return (
        <Form>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Email address</Form.Label>
              <Form.Control type="email" placeholder="Enter email" />
              <Form.Text className="text-muted" onChange={handleChange}>
                We'll never share your email with anyone else.
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" onChange={handleChange}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicCheckbox">
              <Form.Check type="checkbox" label="Check me out" />
            </Form.Group>

            <Button variant="primary" type="submit" onClick={handleSubmit}>
              Submit
            </Button>
        </Form>
    );
}