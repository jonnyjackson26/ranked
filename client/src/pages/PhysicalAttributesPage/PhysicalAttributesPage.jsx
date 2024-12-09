import React, { useState } from "react";
import "./PhysicalAttributesPage.css";

function PhysicalAttributesPage() {
  const [formData, setFormData] = useState({
    heightFeet: "",
    heightInches: "",
    weight: "",
    dash: "",
    benchPress: "",
    deadlift: "",
    squat: "",
    wingspan: "",
    verticalJump: "",
    heartRate: "",
    vo2Max: "",
    dominantHand: "no-selection",
    eyeColor: "no-selection",
    hairColor: "no-selection",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Convert height to inches
    const totalHeightInches =
      parseInt(formData.heightFeet || 0) * 12 + parseInt(formData.heightInches || 0);

    // Prepare data to send
    const dataToSend = {
      height: totalHeightInches,
      weight: formData.weight,
      fastest_40_yard_dash: formData.dash,
      bench_press_max: formData.benchPress,
      deadlift_max: formData.deadlift,
      squat_max: formData.squat,
      wingspan: formData.wingspan,
      vertical_jump_height: formData.verticalJump,
      resting_heart_rate: formData.heartRate,
      vo2_max: formData.vo2Max,
      dominant_hand: formData.dominantHand,
      eye_color: formData.eyeColor,
      hair_color: formData.hairColor,
    };

    try {
      const response = await fetch("/physical-attributes/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dataToSend),
      });

      if (response.ok) {
        alert("Data submitted successfully!");
      } else {
        alert("Something went wrong. Please try again.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error submitting data.");
    }
  };

  return (
    <div className="physical-attributes-page">
      <h1>Physical Attributes</h1>
      <form onSubmit={handleSubmit} className="attributes-form">
        <div className="form-group">
          <label>Height</label>
          <div className="height-inputs">
            <input
              type="number"
              name="heightFeet"
              placeholder="Feet"
              value={formData.heightFeet}
              onChange={handleChange}
            />
            <input
              type="number"
              name="heightInches"
              placeholder="Inches"
              value={formData.heightInches}
              onChange={handleChange}
            />
          </div>
        </div>
        <div className="form-group">
          <label>Weight (lbs)</label>
          <input
            type="number"
            name="weight"
            value={formData.weight}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Fastest 40-Yard Dash (sec)</label>
          <input
            type="number"
            name="dash"
            value={formData.dash}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Bench Press Max (lbs)</label>
          <input
            type="number"
            name="benchPress"
            value={formData.benchPress}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Deadlift Max (lbs)</label>
          <input
            type="number"
            name="deadlift"
            value={formData.deadlift}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Squat Max (lbs)</label>
          <input
            type="number"
            name="squat"
            value={formData.squat}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Wingspan (inches)</label>
          <input
            type="number"
            name="wingspan"
            value={formData.wingspan}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Vertical Jump Height (inches)</label>
          <input
            type="number"
            name="verticalJump"
            value={formData.verticalJump}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Resting Heart Rate (bpm)</label>
          <input
            type="number"
            name="heartRate"
            value={formData.heartRate}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>VO2 Max (if known)</label>
          <input
            type="number"
            name="vo2Max"
            value={formData.vo2Max}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Dominant Hand</label>
          <select
            name="dominantHand"
            value={formData.dominantHand}
            onChange={handleChange}
          >
            <option value="no-selection">See options</option>
            <option value="right">Right</option>
            <option value="left">Left</option>
            <option value="ambidextrous">Ambidextrous</option>
          </select>
        </div>
        <div className="form-group">
          <label>Eye Color</label>
          <select
            name="eyeColor"
            value={formData.eyeColor}
            onChange={handleChange}
          >
            <option value="no-selection">See options</option>
            <option value="brown">Brown</option>
            <option value="blue">Blue</option>
            <option value="green">Green</option>
            <option value="hazel">Hazel</option>
            <option value="gray">Gray</option>
            <option value="amber">Amber</option>
          </select>
        </div>
        <div className="form-group">
          <label>Hair Color</label>
          <select
            name="hairColor"
            value={formData.hairColor}
            onChange={handleChange}
          >
            <option value="no-selection">See options</option>
            <option value="black">Black</option>
            <option value="brown">Brown</option>
            <option value="blonde">Blonde</option>
            <option value="red">Red</option>
            <option value="gray">Gray</option>
            <option value="white">White</option>
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default PhysicalAttributesPage;
