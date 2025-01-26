import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import '../style/Sidebar.css';
import '../style/Button.css';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom'

function Side({ openClass }) {
  return (
    <Container fluid>
      <Row> 
        <Col xs={9}>
          <Navbar className={openClass === 'open' ? 'opneSidebar' : ''} id="sidebar-wrapper" >
            <Link to={"https://kapamais.netlify.app"} target='_blank'>
              <button type="button" className="button" >
              <Navbar.Brand>Profile</Navbar.Brand>
              </button>
            </Link>
            <Link to={"/home"}>
              <button type="button" className="button">
                <Navbar.Brand>Dashboard</Navbar.Brand>
              </button>
            </Link>
            <Link to={"/map"}>
              <button type="button" className="button">
                <Navbar.Brand>HeatMap</Navbar.Brand>
              </button>
            </Link>
            <Link to={"/up_list"}>
              <button type="button" className="button">
                <Navbar.Brand>UpcomingList</Navbar.Brand>
              </button>
            </Link>
          </Navbar> 
        </Col>
      </Row>
    </Container>

    
  );
}

export default Side;