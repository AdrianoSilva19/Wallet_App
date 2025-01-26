import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import '../style/Home.css'; 
import  '../style/Sidebar.css';

function HomeScreen() {
  return (
    <Container fluid>

      <Row>
      <Col xs={9} id="page-content-wrapper" >
          <div className="content">
            <strong>Welcome to <b>Your</b> Dashboard!</strong>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default HomeScreen;