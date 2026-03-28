import React from "react";
import { tractorCatalog, offers } from "../data/tractorCatalog";
import { useNavigate } from "react-router-dom";

const Catalog = () => {
  const navigate = useNavigate();

  return (
    <div style={{ padding: 20 }}>
      <h2>🚜 Tractor Catalog</h2>

      {/* Offers Section */}
      <div style={{ background: "#eef", padding: 10, marginBottom: 20 }}>
        <h3>🔥 Current Offers</h3>
        {offers.map((offer, index) => (
          <p key={index}>{offer}</p>
        ))}
      </div>

      {/* Tractor List */}
      <div style={{ display: "flex", gap: 20 }}>
        {tractorCatalog.map((tractor) => (
          <div
            key={tractor.id}
            style={{
              border: "1px solid #ccc",
              padding: 10,
              width: 250,
            }}
          >
            <img src={tractor.image} alt={tractor.name} width="100%" />
            <h4>{tractor.name}</h4>
            <p>{tractor.hp}</p>
            <p>{tractor.price}</p>

            <button onClick={() => navigate(`/tractor/${tractor.id}`)}>
              Details
            </button>

            <p>
              📍{" "}
              <a href={tractor.showroomLocation} target="_blank">
                Showroom Location
              </a>
            </p>

            <p>
              📞{" "}
              <a href={`tel:${tractor.mobile}`}>
                {tractor.mobile}
              </a>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Catalog;
