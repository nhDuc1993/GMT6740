import { stringify } from "querystring";
import React, { Children, useState } from "react";
import api from "../api";
import "bootstrap/dist/css/bootstrap.css";
import "./Form.css";

interface props {
  handleFormSubmit: (event: React.FormEvent<HTMLFormElement>) => void;
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

const Form = () => {
  const [formData, setFormData] = useState({
    maker: "",
    model: "",
    mileage: 0,
  });

  const [res, setRes] = useState({ data: 0 });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  const handleFormSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setRes(await api.post("./submission", formData));
    console.log(res.data);
  };

  return (
    <div className="container custom-container ">
      <form onSubmit={handleFormSubmit}>
        <div className="custom-padding mb-3 mt-3">
          <label htmlFor="maker" className="form-label">
            Maker
          </label>
          <input
            type="text"
            className="form-control"
            id="maker"
            name="maker"
            onChange={handleChange}
            placeholder="type something..."
            value={formData.maker}
          ></input>
        </div>

        <div className="custom-padding mb-3 mt-3">
          <label htmlFor="model" className="form-label">
            Model
          </label>
          <input
            type="text"
            className="form-control"
            id="model"
            name="model"
            onChange={handleChange}
            placeholder="type something..."
            value={formData.model}
          ></input>
        </div>

        <div className="custom-padding mb-3 mt-3">
          <label htmlFor="mileage" className="form-label">
            Mileage
          </label>
          <input
            type="number"
            className="form-control"
            id="mileage"
            name="mileage"
            onChange={handleChange}
            placeholder="type something..."
            value={formData.mileage}
          ></input>
        </div>

        <div className="custom-padding mb-3 mt-3">
          <button type="submit" className="btn btn-primary">
            {" "}
            Submit
          </button>
        </div>
      </form>
      <div className="custom-padding mb-3 mt-3">
        <p>The estimate price of this car is €{res.data}</p>
      </div>
    </div>
  );
};

export default Form;
