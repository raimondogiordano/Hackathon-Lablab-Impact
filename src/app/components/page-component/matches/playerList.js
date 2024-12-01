"use client";
import React, { useEffect, useState } from "react";
import { IoCalendar } from "react-icons/io5";
import { TbSoccerField } from "react-icons/tb";
import { RiTeamFill } from "react-icons/ri";
import { MdOutlineScoreboard } from "react-icons/md";
import { MdDelete } from "react-icons/md";
import { Hug } from "../../ui/utils";
import useModal from "@/app/hooks/useModal";
import { BasicModal, OffsetLeftModal } from "../../ui/modals";
import { RoundedSwitch } from "../../ui/switches";
import localStorageManager from "@/utils/localStorageManager";
import moment from "moment";

const PlayerList = ({
  players,
  isAdmin,
  match,
  onJoin,
  onLeave,
  onTeamChange,
  onInitModal,
  onSave,
  onChangeMatch,
  onChangeGks,
  onChangeBlack,
  onChangePink,
  pinkScore,
  blackScore,
}) => {
  const modal = useModal();
  const user = localStorageManager.getItem("user");
  const [loading, setloading] = useState(true);
  useEffect(() => {
    setloading(false);
  }, []);

  const onManage = () => {
    modal.openModal();
  };
  const onLeaveWrap = () => {
    const p = players.find((p) => p.player._id === user.player._id);

    onLeave(p);
  };
  const onRemove = (ply) => {
    const p = players.find((p) => p.player._id === ply.player._id);

    onLeave(p);
  };
  const sortedPlayers = players.sort((a, b) =>
    new Date(a.exact) > new Date(b.exact) ? 1 : -1
  );

  const handleSave = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    await onSave();
    modal.closeModal();
  };
  const gks = sortedPlayers.filter((p) => p?.player?.role === "P");
  const moveplayers = sortedPlayers.filter((p) => p?.player?.role !== "P");
  const isIn = !!players.find((p) => p?.player?._id === user.player._id);

  const teamClasses = {
    PINK: "bg-pink-600 h-[20px] w-[20px] block rounded-full",
    BLACK:
      "bg-black h-[20px] w-[20px] block rounded-full dark:border-[0.5px] dark:border-[#c6c6c6]",
  };

  return (
    <div className="flex flex-col h-full bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text p-4 rounded-lg border border-light-border dark:border-dark-border">
      {!loading && (
        <>
          {/* Lista dei Giocatori */}
          <div className="flex-1 overflow-y-auto mb-4">
            {players.length === 0 && (
              <p className="text-center">Nessun giocatore presente</p>
            )}
            <ul>
              {match.gks &&
                gks.map((player, index) => (
                  <>
                    {index <= 1 && (
                      <li
                        key={index}
                        className="flex items-center justify-between p-2 mb-2 border border-light-border dark:border-dark-border rounded-lg bg-light-background dark:bg-dark-background"
                      >
                        {player.player.name + "(GK)"}
                        {player.team && (
                          <button className={teamClasses[player.team]}></button>
                        )}
                      </li>
                    )}
                  </>
                ))}
              {match.gks &&
                moveplayers.map((player, index) => (
                  <div key={index}>
                    {index ===
                      14 - gks.filter((g, index) => index <= 1).length && (
                      <>
                        <br />
                        <h6 className="ml-2 font-bold">Riserve</h6>
                        <br />
                      </>
                    )}
                    <li
                      key={index}
                      className="flex items-center justify-between p-2 mb-2 border border-light-border dark:border-dark-border rounded-lg bg-light-background dark:bg-dark-background"
                    >
                      {player.player.name}
                      {player.team && (
                        <button className={teamClasses[player.team]}></button>
                      )}
                    </li>{" "}
                  </div>
                ))}
              {match.gks && gks.length > 1 && (
                <>
                  <br />
                  <h6 className="ml-2 font-bold">Riserve Portieri</h6>
                  <br />
                </>
              )}
              {match.gks &&
                gks.map((player, index) => (
                  <>
                    {index > 1 && (
                      <li
                        key={index}
                        className="flex items-center justify-between p-2 mb-2 border border-light-border dark:border-dark-border rounded-lg bg-light-background dark:bg-dark-background"
                      >
                        {player.player.name + "(GK)"}
                      </li>
                    )}
                  </>
                ))}
              {!match.gks &&
                sortedPlayers.map((player, index) => (
                  <div key={index}>
                    {index === 14 && (
                      <>
                        <br />
                        <h6 className="ml-2 font-bold">Riserve</h6>
                        <br />
                      </>
                    )}
                    <li
                      key={index}
                      className="flex items-center justify-between p-2 mb-2 border border-light-border dark:border-dark-border rounded-lg bg-light-background dark:bg-dark-background"
                    >
                      {player.player.name}
                      {player.team && (
                        <button className={teamClasses[player.team]}></button>
                      )}
                    </li>{" "}
                  </div>
                ))}
            </ul>
          </div>

          {/* Action Bar */}
          <div className="flex flex-col lg:flex-row  items-center justify-between p-2 border-t border-light-border dark:border-dark-border bg-light-background dark:bg-dark-background">
            <div className="text-sm w-full h-full ml-8 mb-2 lg:m-0 lg:w-fit">
              <Hug>
                <IoCalendar />{" "}
                <p className="ml-2">
                  {moment(match.date.split(".")[0]).format("DD/MM/YY HH:mm") ||
                    moment(Date.now()).format("DD/MM/YY HH:mm")}
                </p>
              </Hug>
              <Hug>
                <TbSoccerField />
                <p className="ml-2">{match?.location || "Mazzone"}</p>
              </Hug>
              <Hug>
                <RiTeamFill /> <p className="ml-2"> {players.length}</p>
              </Hug>
            </div>
            <div className="text-sm w-full h-full ml-8 mb-4 lg:m-0 lg:w-fit">
              <Hug>
                <MdOutlineScoreboard />{" "}
                <p className="ml-2 font-bold">
                  {match?.result || "PINK - BLACK 0-0"}
                </p>
              </Hug>
            </div>
            <div className="space-x-2">
              {isAdmin && (
                <button
                  onClick={onManage}
                  className="p-2 bg-utils-action text-white rounded-lg"
                >
                  Gestisci
                </button>
              )}
              {!isIn && (
                <button
                  onClick={() => onJoin(user.player)}
                  className="p-2 bg-accent-background text-accent-text rounded-lg"
                >
                  Prenotati
                </button>
              )}
              {isIn && (
                <button
                  onClick={() => onLeaveWrap()}
                  className="p-2 bg-utils-error text-white rounded-lg"
                >
                  Rimuoviti
                </button>
              )}
            </div>
          </div>
          <BasicModal modal={modal}>
            <div className="text-xs">
              <h2 className="text-lg font-bold text-light-text dark:text-dark-text">
                Info Partita
              </h2>
              <div className="flex-1 overflow-y-auto mb-4 mt-8">
                <ul>
                  {sortedPlayers.map((player, index) => (
                    <div key={index}>
                      {index === 14 && (
                        <>
                          <br />
                          <h6 className="ml-2 font-bold">Riserve</h6>
                          <br />
                        </>
                      )}
                      <li
                        key={index}
                        className="flex items-center justify-between p-2 mb-2 border border-light-border dark:border-dark-border rounded-lg bg-light-background dark:bg-dark-background"
                      >
                        {player.player.name}
                        <div className="flex gap-2 mt-1">
                          <button
                            onClick={() => onTeamChange(player, "PINK")}
                            className={`bg-pink-600 h-[20px] w-[20px] block rounded-full ${
                              player.team === "PINK"
                                ? "border-2 border-accent-linkDark"
                                : ""
                            } `}
                          ></button>
                          <button
                            onClick={() => onTeamChange(player, "BLACK")}
                            className={`bg-black h-[20px] w-[20px] block rounded-full  ${
                              player.team === "BLACK"
                                ? "border-2 border-accent-linkDark"
                                : "dark:border-[0.5px] dark:border-[#c6c6c6]"
                            }`}
                          ></button>
                          <button
                            onClick={() => onRemove(player)}
                            className="h-[20px] w-[20px] block rounded-full text-lg"
                          >
                            <MdDelete />{" "}
                          </button>
                          <button></button>
                        </div>
                      </li>{" "}
                    </div>
                  ))}
                </ul>
              </div>
              <div className="rounded-md flex flex-col gap-3">
                <div className="flex flex-col items-start justify-between">
                  <div className="space-y-5">
                    <h6 className="ml-2 font-bold">Data</h6>
                    <br />
                    <input
                      type="datetime-local"
                      value={match.date}
                      className="p-2 border w-full border-light-border dark:border-dark-border rounded-lg focus:outline-none bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text uppercase"
                      name="date"
                      onChange={onChangeMatch}
                    />
                  </div>
                  <div className="flex flex-col items-start justify-between">
                    <h6 className="ml-2 font-bold">Luogo</h6>
                    <br />
                    <input
                      type="text"
                      value={match.location}
                      name="location"
                      onChange={onChangeMatch}
                      className="p-2 w-full border border-light-border dark:border-dark-border rounded-lg focus:outline-none bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text"
                      placeholder="Campo"
                    />
                  </div>
                  <div className="flex flex-col items-start justify-between">
                    <h6 className="ml-2 font-bold">Ruolo portieri</h6>
                    <br />
                    <RoundedSwitch onChange={onChangeGks} checked={match.gks} />
                  </div>
                  <div className="flex flex-col items-start justify-between">
                    <h6 className="ml-2 font-bold">Risultato</h6>
                    <br />
                    <div className="flex gap-2 pl-2">
                      <div>
                        PINK{" "}
                        <input
                          value={pinkScore}
                          onChange={onChangePink}
                          type="number"
                          className="p-2 w-full border border-light-border dark:border-dark-border rounded-lg focus:outline-none bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text"
                          placeholder="0"
                        />
                      </div>
                      <div>
                        BLACK{" "}
                        <input
                          onChange={onChangeBlack}
                          value={blackScore}
                          type="number"
                          className="p-2 w-full border border-light-border dark:border-dark-border rounded-lg focus:outline-none bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text"
                          placeholder="0"
                        />
                      </div>
                    </div>
                  </div>
                </div>
                <div>
                  <button
                    onClick={handleSave}
                    className="p-2 bg-accent-background text-accent-text rounded-lg"
                  >
                    Salva
                  </button>
                </div>
              </div>
            </div>
          </BasicModal>
        </>
      )}
    </div>
  );
};
export default PlayerList;
