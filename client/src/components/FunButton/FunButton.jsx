import React from "react";
import "./FunButton.css";
import { Link } from "react-router-dom";

const FunButton = ({ onClick }) => {
  return (
    <Link to="/stats" className="see-how-i-rank-button">
      See How I Rank
    </Link>
  );
};

export default FunButton;
