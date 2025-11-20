-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`device_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`device_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `device_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`give_service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`give_service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `describtion` VARCHAR(45) NOT NULL,
  `service_time` DATE NOT NULL,
  `device_condition` VARCHAR(45) NOT NULL,
  `device_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_give_service_device_type1_idx` (`device_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_give_service_device_type1`
    FOREIGN KEY (`device_type_id`)
    REFERENCES `mydb`.`device_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`category` (
  `category_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`category_id`));


-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);


-- -----------------------------------------------------
-- Table `mydb`.`timestamps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`timestamps` (
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL);


-- -----------------------------------------------------
-- Table `mydb`.`room_location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`room_location` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `room` VARCHAR(45) NOT NULL,
  `desk` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`office_location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`office_location` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `office_adress` VARCHAR(45) NOT NULL,
  `room_location_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_office_location_room_location1_idx` (`room_location_id` ASC) VISIBLE,
  CONSTRAINT `fk_office_location_room_location1`
    FOREIGN KEY (`room_location_id`)
    REFERENCES `mydb`.`room_location` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`employee` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`workplace`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`workplace` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NOT NULL,
  `office_location_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_workplace_employee1_idx` (`employee_id` ASC) VISIBLE,
  INDEX `fk_workplace_office_location1_idx` (`office_location_id` ASC) VISIBLE,
  CONSTRAINT `fk_workplace_employee1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `mydb`.`employee` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_workplace_office_location1`
    FOREIGN KEY (`office_location_id`)
    REFERENCES `mydb`.`office_location` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`repair_service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`repair_service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `describtion` VARCHAR(45) NOT NULL,
  `service_time` DATE NOT NULL,
  `device_condition` VARCHAR(45) NOT NULL,
  `device_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_repair_service_device_type1_idx` (`device_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_repair_service_device_type1`
    FOREIGN KEY (`device_type_id`)
    REFERENCES `mydb`.`device_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`exchange_service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`exchange_service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `describtion` VARCHAR(45) NOT NULL,
  `service_time` DATE NOT NULL,
  `device_condition` VARCHAR(45) NOT NULL,
  `device_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_exchange_service_device_type1_idx` (`device_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_exchange_service_device_type1`
    FOREIGN KEY (`device_type_id`)
    REFERENCES `mydb`.`device_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`update_service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`update_service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `describtion` VARCHAR(45) NOT NULL,
  `service_time` DATE NOT NULL,
  `device_condition` VARCHAR(45) NOT NULL,
  `device_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_update_service_device_type1_idx` (`device_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_update_service_device_type1`
    FOREIGN KEY (`device_type_id`)
    REFERENCES `mydb`.`device_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`bugfix_service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`bugfix_service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `describtion` VARCHAR(45) NOT NULL,
  `service_time` DATE NOT NULL,
  `device_condition` VARCHAR(45) NOT NULL,
  `device_type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_bugfix_service_device_type1_idx` (`device_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_bugfix_service_device_type1`
    FOREIGN KEY (`device_type_id`)
    REFERENCES `mydb`.`device_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`workplace_give`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`workplace_give` (
  `give_service_id` INT NOT NULL,
  `workplace_id` INT NOT NULL,
  INDEX `fk_workplace_give_give_service_idx` (`give_service_id` ASC) VISIBLE,
  INDEX `fk_workplace_give_workplace1_idx` (`workplace_id` ASC) VISIBLE,
  CONSTRAINT `fk_workplace_give_give_service`
    FOREIGN KEY (`give_service_id`)
    REFERENCES `mydb`.`give_service` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_workplace_give_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `mydb`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`workplace_update`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`workplace_update` (
  `update_service_id` INT NOT NULL,
  `workplace_id` INT NOT NULL,
  INDEX `fk_workplace_update_update_service1_idx` (`update_service_id` ASC) VISIBLE,
  INDEX `fk_workplace_update_workplace1_idx` (`workplace_id` ASC) VISIBLE,
  CONSTRAINT `fk_workplace_update_update_service1`
    FOREIGN KEY (`update_service_id`)
    REFERENCES `mydb`.`update_service` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_workplace_update_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `mydb`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`workplace_exchange`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`workplace_exchange` (
  `exchange_service_id` INT NOT NULL,
  `workplace_id` INT NOT NULL,
  INDEX `fk_workplace_exchange_exchange_service1_idx` (`exchange_service_id` ASC) VISIBLE,
  INDEX `fk_workplace_exchange_workplace1_idx` (`workplace_id` ASC) VISIBLE,
  CONSTRAINT `fk_workplace_exchange_exchange_service1`
    FOREIGN KEY (`exchange_service_id`)
    REFERENCES `mydb`.`exchange_service` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_workplace_exchange_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `mydb`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`workplace_repair`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`workplace_repair` (
  `repair_service_id` INT NOT NULL,
  `workplace_id` INT NOT NULL,
  INDEX `fk_workplace_repair_repair_service1_idx` (`repair_service_id` ASC) VISIBLE,
  INDEX `fk_workplace_repair_workplace1_idx` (`workplace_id` ASC) VISIBLE,
  CONSTRAINT `fk_workplace_repair_repair_service1`
    FOREIGN KEY (`repair_service_id`)
    REFERENCES `mydb`.`repair_service` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_workplace_repair_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `mydb`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`workplace_bugfix`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`workplace_bugfix` (
  `bugfix_service_id` INT NOT NULL,
  `workplace_id` INT NOT NULL,
  INDEX `fk_workplace_bugfix_bugfix_service1_idx` (`bugfix_service_id` ASC) VISIBLE,
  INDEX `fk_workplace_bugfix_workplace1_idx` (`workplace_id` ASC) VISIBLE,
  CONSTRAINT `fk_workplace_bugfix_bugfix_service1`
    FOREIGN KEY (`bugfix_service_id`)
    REFERENCES `mydb`.`bugfix_service` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_workplace_bugfix_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `mydb`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
