DELIMITER //

CREATE PROCEDURE GetAllArtists()
BEGIN
	SELECT *  FROM Artist;
END //

DELIMITER ;