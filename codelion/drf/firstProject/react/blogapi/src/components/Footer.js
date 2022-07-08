import React from 'react';
import {Link} from 'react-router-dom';


export default function Footer() {
    const footers = [
        {
            title: 'Company',
            description: [
                'Team', 
                'History', 
                'Contact us', 
                'Locations']
        },
        {
            title: 'Features',
            description: [
                'Cool stuff',
                'Random feature',
                'Team feature',
                'Developer stuff',
                'Another one',
            ]
        },
        {
            title: 'Resources',
            description: [
                'Resource',
                'Resource name',
                'Another resource',
                'Final resource',
            ]
        }, 
        {
            title: 'Legal',
            description: ['Privacy policy', 'Terms of use']
        }
    ]
    return (
        <footer className="py-5 bg-dark mt-auto">
            <div className="row">
                {footers.map((footer) => (
                    <div className="col" key={footer.title}>
                        <h4 style={{color : "white"}}>
                            {footer.title}
                        </h4>
                        <ul>
                            {footer.description.map((item) => 
                                <li key={item}>
                                    <Link to="/">{item}</Link>
                                </li>
                            )}
                        </ul>
                    </div>
                ))}
            </div>
        </footer>
    );
}