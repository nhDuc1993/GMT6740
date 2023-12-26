import React from "react";

const Banner = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-warning-subtle">
      <div className="container-fluid">
        <a className="navbar-brand" href={window.location.pathname}>
          Car Price Prediction
        </a>
      </div>
    </nav>
  );
};

export default Banner;
