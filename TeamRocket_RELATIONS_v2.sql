CREATE TABLE User (
  userID          CHAR(25),
  name            VARCHAR,
  average_stars   FLOAT,
  fans            INT,
  cool            INT,
  funny           INT,
  useful          INT,  
  yelping_since   DATE,
  tip_count       INT, -- DEFAULT 0
  total_likes     INT, -- DEFAULT 0
  user_latitude   FLOAT,
  user_longitude  FLOAT,
  PRIMARY KEY (userID)
);

CREATE TABLE Business (
  businessID      CHAR(25),
  name            VARCHAR,
  city            VARCHAR,
  state           VARCHAR,
  zipcode         VARCHAR,
  latitude        FLOAT,
  longitude       FLOAT,
  address         VARCHAR,
  num_tips        INT, -- DEFAULT 0
  num_checkins    INT, -- DEFAULT 0
  is_open         VARCHAR,
  stars           INT, -- DEFAULT 0
  PRIMARY KEY (businessID)
);

CREATE TABLE Checkins (
  businessID      CHAR(25),
  year            INT,
  month           CHAR (12),
  day             INT,
  time            VARCHAR,
  PRIMARY KEY(businessID, year, month, day, time),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);

CREATE TABLE Hours (
  businessID      CHAR(25),
  dayOfWeek       CHAR(10),
  open            VARCHAR,
  close           VARCHAR,
  PRIMARY KEY(businessID, dayOfWeek),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);

CREATE TABLE Attributes (
  businessID      CHAR(25),
  attr_name       VARCHAR,
  value           INT,
  PRIMARY KEY(businessID, attr_name),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);

CREATE TABLE Categories (
  businessID      CHAR(25),
  category_name   VARCHAR,
  PRIMARY KEY(businessID, category_name),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);

CREATE TABLE Friend (
  userID          CHAR(25),
  friendID        CHAR(25),
  PRIMARY KEY(userID, friendID),
  FOREIGN KEY(userID) REFERENCES User(userID),
  FOREIGN KEY(friendID) REFERENCES User(userID)
);

CREATE TABLE Tip (
  userID          CHAR(25),
  businessID      CHAR(25),
  time_stamp      DATE,
  num_likes       INT,
  description     VARCHAR,
  PRIMARY KEY(userID, businessID, time_stamp),
  FOREIGN KEY(userID) REFERENCES User(userID),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);

CREATE TABLE SearchesFor (
  userID          CHAR(25),
  businessID      CHAR(25),
  distance        FLOAT,
  PRIMARY KEY(userID, businessID),
  FOREIGN KEY(userID) REFERENCES User(userID),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);

CREATE TABLE TipLikes (
  userID          CHAR(25),
  businessID      CHAR(25),
  PRIMARY KEY(userID, businessID)
  FOREIGN KEY(userID) REFERENCES User(userID),
  FOREIGN KEY(businessID) REFERENCES Business(businessID)
);


