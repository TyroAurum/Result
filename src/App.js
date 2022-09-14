import React, { useState } from 'react';
import LoginCard from './jsx/login';
//import ResultCard from './page/result';
import "./App.css"
import "./alogincard.css";

const App=() => {
  const [isAuthenticaed,setIsAuthenticated] = useState(JSON.parse(localStorage.getItem('auth')) || false);
  return (<><div>
              <LoginCard />
            </div>
    </>
  );
};

export default App;
