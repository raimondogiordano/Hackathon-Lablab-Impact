"use client";
import "@/app/components/styles/chat.css";
import React, { useState } from "react";
import { FiMic, FiSend } from "react-icons/fi"; // Assicurati di avere installato react-icons

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim()) {
      const newMessage = { text: input, sender: "user" };
      setMessages([...messages, newMessage]);
      setInput("");

      // Simulate chatbot response
      setTimeout(() => {
        const botMessage = { text: `You said: ${input}`, sender: "bot" };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      }, 1000);
    }
  };

  const handleRecord = () => {
    alert("Voice recording functionality is not implemented yet.");
  };

  return (
    <div className="flex flex-col h-full max-h-[94vh] p-0 md:p-4 lg:p-4 xl:p-4 bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text rounded-lg md:border lg:border xl:border border-light-border dark:border-dark-border">
      <div className="flex-1 overflow-y-auto mb-4 ">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${
              message.sender === "user" ? "justify-end" : "justify-start"
            } mb-2 w-full`}
          >
            <div
              className={`p-[1.2rem] pb-[2rem] rounded-lg max-w-[80%] min-w-[15%] ${
                message.sender === "user"
                  ? "bg-accent-background text-accent-text"
                  : "bg-light-background dark:bg-dark-background border border-light-border dark:border-dark-border"
              }`}
            >
              {message.text}
            </div>
          </div>
        ))}
      </div>
      <div className="flex items-center space-x-0 md:space-x-1 lg:space-x-1 xl:space-x-1">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 p-2 border border-light-border dark:border-dark-border rounded-lg focus:outline-none bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text"
          placeholder="Type your message..."
        />
        <button
          onClick={handleRecord}
          className="p-2 bg-light-background dark:bg-dark-background md:border lg:border xl:border border-light-border dark:border-dark-border rounded-lg"
        >
          <FiMic className="text-light-text dark:text-dark-text" />
        </button>
        <button
          onClick={handleSend}
          className="p-2 bg-accent-background text-accent-text rounded-lg"
        >
          <FiSend />
        </button>
      </div>
    </div>
  );
};

export default ChatPage;