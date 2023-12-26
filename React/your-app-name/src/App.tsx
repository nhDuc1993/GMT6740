import React, { Children, useState } from "react";

import "bootstrap/dist/css/bootstrap.css";
import Banner from "./components/Banner";
import Form from "./components/Form";

function App() {
  return (
    <>
      <div>
        <Banner />
      </div>
      <div>
        <Form />
      </div>
    </>
  );
}

export default App;
