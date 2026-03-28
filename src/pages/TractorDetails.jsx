import React from "react";
import { useParams } from "react-router-dom";
import { tractorCatalog } from "../data/tractorCatalog";

const TractorDetails = () => {
  const { id } = useParams();
  const tractor = tractorCatalog.find((t) => t.id === Number(id));

  if (!tractor) return <h2>Tractor Not Found</h2>;

  const whatsappMessage = `https://wa.me/${tractor.mobile}?text=I am interested in purchasing ${tractor.name}`;

  return (
    <div style={{ padding: 20 }}>
      <h2>{tractor.name}</h2>
      <img src={tractor.image} width="300" />

      <p><b>HP:</b> {tractor.hp}</p>
      <p><b>Fuel:</b> {tractor.fuel}</p>
      <p><b>Price:</b> {tractor.price}</p>
      <p>{tractor.description}</p>

      <a href={whatsappMessage} target="_blank">
        <button>🟢 Add to Cart (WhatsApp)</button>
      </a>
    </div>
  );
};

export default TractorDetails;
