import { useEffect, useState } from "react";
import { FaDollarSign, FaPercentage, FaGlobe } from "react-icons/fa";
import API from "../api/api";
import KPICard from "../components/KPICard";
import RevenueChart from "../components/RevenueChart";
import Chat from "./Chat";

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [trends, setTrends] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const summaryRes = await API.get("/api/summary");
      const trendsRes = await API.get("/api/trends");

      setSummary(summaryRes.data);
      setTrends(trendsRes.data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!summary) {
    return <h2>Loading Dashboard...</h2>;
  }

  return (
    <>
      <nav className="navbar">
        <div className="logo">🌿 NovaBite</div>
        <div className="nav-right">📊 Sales Analytics</div>
      </nav>

      <div className="dashboard">

        <div className="hero">
          <h1>NovaBite Sales Dashboard</h1>
          <p>AI-Powered Business Insights & Analytics</p>
        </div>

        <Chat />

        <div className="kpi-grid">

          <KPICard
            title="Total Revenue"
            value={`$${summary.total_net_revenue.toLocaleString()}`}
            icon={<FaDollarSign />}
            type="revenue"
          />

          <KPICard
            title="Gross Profit Margin"
            value={`${summary.gross_profit_margin}%`}
            icon={<FaPercentage />}
            type="margin"
          />

          <KPICard
            title="Top Region"
            value={summary.top_region}
            icon={<FaGlobe />}
            type="region"
          />

        </div>

        <RevenueChart data={trends} />

      </div>
    </>
  );
}

export default Dashboard;