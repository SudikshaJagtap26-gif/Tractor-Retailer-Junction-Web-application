import { BrowserRouter, Routes, Route } from "react-router-dom";
import Catalog from "./pages/Catalog";
import TractorDetails from "./pages/TractorDetails";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Catalog />} />
        <Route path="/tractor/:id" element={<TractorDetails />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
