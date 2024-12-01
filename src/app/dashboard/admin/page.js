"use client";
import React, { useState, useEffect, useRef } from "react";
import { Chart, ArcElement, PieController, BarController, BarElement, CategoryScale, LinearScale, Tooltip } from 'chart.js';
import { Pie, Bar } from 'react-chartjs-2';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import proposalsData from "@/utils/proposalsData";

Chart.register(ArcElement, PieController, BarController, BarElement, CategoryScale, LinearScale, Tooltip);

function AdminDashboard() {
  const [proposals, setProposals] = useState(proposalsData);
  const mapRef = useRef();

  useEffect(() => {
    if (mapRef.current && proposals.length > 0) {
      const map = mapRef.current;
      const bounds = L.latLngBounds(
        proposals.map((proposal) => {
          const [lat, lng] = proposal.geo_point.split(",").map(Number);
          return [lat, lng];
        })
      );
      map.fitBounds(bounds, { padding: [20, 20] }); // Aggiunge padding ai limiti per una migliore visualizzazione
    }
  }, [proposals]);

  // Prepara i dati per i grafici
  const labelCounts = proposals.reduce((acc, proposal) => {
    proposal.labels.forEach((label) => {
      acc[label] = (acc[label] || 0) + 1;
    });
    return acc;
  }, {});

  const quartierCounts = proposals.reduce((acc, proposal) => {
    acc[proposal.quartiere] = (acc[proposal.quartiere] || 0) + 1;
    return acc;
  }, {});

  const chartData = {
    labels: Object.keys(labelCounts),
    datasets: [
      {
        label: 'Numero di Proposte per Categoria',
        data: Object.values(labelCounts),
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)',
          'rgba(255, 159, 64, 0.6)'
        ]
      }
    ]
  };

  const quartierChartData = {
    labels: Object.keys(quartierCounts),
    datasets: [
      {
        label: 'Numero di Proposte per Quartiere',
        data: Object.values(quartierCounts),
        backgroundColor: [
          'rgba(255, 159, 64, 0.6)',
          'rgba(153, 102, 255, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(255, 99, 132, 0.6)'
        ]
      }
    ]
  };

  return (
    <div className="p-4">
      <div className="flex justify-center items-center mb-4">
        <h1 className="text-xl font-semibold">Proposte dei Quartieri - Bologna</h1>
      </div>

      {/* Grafici Statistici */}
      <div className="mb-8">
        <h2 className="text-lg font-semibold mb-4">Statistiche delle Proposte</h2>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 h-96">
          <div className="w-full h-96">
            <Pie 
              data={chartData} 
              options={{ 
                maintainAspectRatio: false,
                plugins: { 
                  legend: { position: 'bottom' },
                }
              }}
            />
            <p className="text-center mt-2 text-sm font-medium">Numero di Proposte</p>
          </div>
          <div className="w-full h-96">
            <Bar 
              data={chartData} 
              options={{ 
                maintainAspectRatio: false,
                scales: {
                  y: {
                    beginAtZero: true,
                    ticks: {
                      precision: 0 // Imposta la precisione a 0 per evitare valori decimali
                    }
                  },
                  x:{
                    display:false
                  }
                }
              }}
            />
             <p className="text-center mt-2 text-sm font-medium">Numero di Proposte</p>
          </div>
          <div className="w-full h-96">
            <Pie 
              data={quartierChartData} 
              options={{ 
                maintainAspectRatio: false,
                plugins: { 
                  legend: { position: 'bottom' },
                  tooltip: { // Aggiunta delle descrizioni delle opzioni
                    callbacks: {
                      label: function (context) {
                        return `${context.label}: ${context.raw}`;
                      }
                    }
                  }
                } 
              }}
            />
            <p className="text-center mt-2 text-sm font-medium">Numero di Proposte per Quartiere</p>
          </div>
          
        </div>
      </div>

      {/* Divider */}
      <div className="border-t border-gray-300 my-8"></div>

      {/* Contenitore della Mappa e della Griglia */}
      <div className="flex flex-col lg:flex-row gap-4 mb-8" style={{ height: '500px' }}>
        {/* Mappa Interattiva */}
        <div className="w-full lg:w-4/5" style={{ height: '100%' }}>
          <h2 className="text-lg font-semibold mb-4">Mappa delle Proposte</h2>
          <MapContainer
            ref={mapRef}
            center={[44.4949, 11.3426]}
            zoom={13}
            style={{ height: '100%', width: '100%' }}
          >
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            {proposals.map((proposal, index) => {
              const [lat, lng] = proposal.geo_point.split(",").map(Number);
              return (
                <Marker key={index} position={[lat, lng]} icon={L.icon({ iconUrl: "https://leafletjs.com/examples/custom-icons/leaf-red.png", iconSize: [25, 41], iconAnchor: [12, 41] })}>
                  <Popup>
                    <strong>{proposal.nome}</strong><br />
                    Quartiere: {proposal.quartiere}<br />
                    Zona di Prossimità: {proposal.zona_prossimita}
                  </Popup>
                </Marker>
              );
            })}
          </MapContainer>
        </div>

        {/* Griglia delle proposte con Scroll */}
        <div className="w-full lg:w-1/5">
          <h2 className="text-lg font-semibold mb-4">Lista delle Proposte</h2>
          <div className="grid grid-cols-1 gap-4 overflow-y-auto" style={{ height: '100%' }}>
            {proposals.map((proposal, index) => (
              <div
                key={index}
                className="bg-light-background dark:bg-dark-background p-4 rounded-lg border border-light-border dark:border-dark-border"
              >
                <h2 className="text-center text-lg font-bold mb-2">{proposal.nome}</h2>
                <p>Quartiere: {proposal.quartiere}</p>
                <p>Zona di prossimità: {proposal.zona_prossimita}</p>
                <div className="mt-2">
                  <span className="text-sm font-semibold">Categorie:</span>
                  <ul className="list-disc ml-4">
                    {proposal.labels && proposal.labels.length > 0 ? (
                      proposal.labels.map((label, labelIndex) => (
                        <li key={labelIndex} className="text-sm">
                          {label}
                        </li>
                      ))
                    ) : (
                      <li className="text-sm">Nessuna categoria disponibile</li>
                    )}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default AdminDashboard;
