import React from 'react';
import './App.css';
import { BrowserRouter, Routes, Route} from 'react-router-dom'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import Content from './components/Content'
import Footer from './components/Footer';
import Register from './components/Register';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <div className='container'>
          <Header />
          <Routes>
            <Route path="/" element={<Content/>} />
            <Route path='/register' element={<Register/>}/>
          </Routes>
          <Footer />
      </div>
      </BrowserRouter>
    </div> 
  );
}

export default App;
