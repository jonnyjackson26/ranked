import React, { useState } from "react";
import "./CanYouPage.css";

const bubblesData = [
  "Solve a Rubik's Cube",
  "Dunk a basketball",
  "Do a backflip",
  "Juggle three balls",
  "Ride a unicycle",
  "Do a cartwheel",
  "Swim",
  "Do 10 push-ups",
  "Do a muscle-up",
  "Touch your toes",
  "Spin a basketball on your finger",
  "Drive a car",
];

const CanYouPage = () => {
  const [selectedBubbles, setSelectedBubbles] = useState([]);

  const handleBubbleClick = async (bubble) => {
    const isSelected = selectedBubbles.includes(bubble);
    const updatedBubbles = isSelected
      ? selectedBubbles.filter((item) => item !== bubble)
      : [...selectedBubbles, bubble];

    setSelectedBubbles(updatedBubbles);

    try {
      const response = await fetch("/i-can/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bubble, isSelected: !isSelected }),
      });

      if (!response.ok) {
        console.error("Failed to update selection");
      }
    } catch (error) {
      console.error("Error sending selection data:", error);
    }
  };

  return (
    <div className="can-you-page">
      <h1 className="page-title">I can...</h1>
      <div className="bubbles-container">
        {bubblesData.map((bubble) => (
          <div
            key={bubble}
            className={`bubble ${
              selectedBubbles.includes(bubble) ? "selected" : ""
            }`}
            onClick={() => handleBubbleClick(bubble)}
          >
            <span className="bubble-text">{bubble}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CanYouPage;
