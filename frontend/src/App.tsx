import React from 'react';

import TopPage from './components/TopPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import VB12 from './components/VB12';
import Glucose
  from './components/Glucose';
function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={
            <TopPage />
          } />
          <Route path="/vb12" element={
            <VB12 />
          } />
          <Route path="/glucose" element={
            <Glucose />
          } />
        </Routes>
      </Router>
    </>
  );
}

export default App;
