import React from 'react';
import {Link} from 'react-router-dom'
import styles from "./Header.module.css";

export default function Header() {
    const contents = [
      {id: 1, title: 'PROJECT', url: 'introduce'},
      {id: 2, title: 'STORY', url: 'story'},
      {id: 3, title: 'PLAN', url: 'plan'},
      {id: 4, title: 'TEAM', url: 'team'},
      {id: 5, title: 'ROADMAP', url: 'roadmap'},
      {id: 6, title: 'PARTNER', url: 'partner'},
    ];

    return (
        <>
        <nav id={styles.navbar} className="navbar navbar-expand-md navbar-light">
            <div className="container-fluid">
              <Link className="navbar-brand" to="/">
                <img src="#" alt=""></img>
              </Link>
              <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="true" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
              </button>
              <div className={`collapse navbar-collapse ${styles.navbarSupportedContent}`} id="navbarSupportedContent">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                  {contents.map((content) => 
                    <li className="nav-item" key={content.id}>
                      <Link className="nav-link" activeClass="active" to={content.url}>{content.title}</Link>
                    </li>
                  )}
                </ul>
              </div>
            </div>
        </nav>
        </>
    );
}