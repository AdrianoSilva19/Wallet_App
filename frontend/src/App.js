import React from 'react';
import { Col } from 'react-bootstrap';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import HomeScreen from './screens/Home';
import Profile from './screens/Profile';
import './style/Home.css';
import Side from './components/sidebar';


function App() {
  const [on, setOn] = React.useState(false);

  const handleOn = () => {
    setOn(!on);
  };
  return (
    <BrowserRouter>
      <aside className={on ? 'to-left' : ''}>
        <button className={`toggle-button ${on ? 'open' : ''}`} onClick={handleOn}></button>
      </aside>
      {on && <Side openClass="open" />}
      <Col xs={9} id="page-content-wrapper">
        <Routes>
          <Route path='/home' element={<HomeScreen />} exact />
          <Route path='/profile' element={<Profile />} exact />
        </Routes>
      </Col>
    </BrowserRouter>
  );
}

export default App;