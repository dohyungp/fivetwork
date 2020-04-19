import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { GoogleLogin } from "react-google-login";

const responseGoogle = (response) => {
  console.log(response);
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <GoogleLogin
          clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
          onSuccess={responseGoogle}
          onFailure={responseGoogle}
          cookiePolicy={"single_host_origin"}
          tag={"a"}
          hostedDomain={process.env.REACT_APP_GOOGLE_HOST_DOMAIN}
        />
      </header>
    </div>
  );
}

export default App;
