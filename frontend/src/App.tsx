import React from 'react';

import TopPage from './components/TopPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={
            <TopPage />
          } />
        </Routes>
      </Router>
    </>
  );
}

export default App;
