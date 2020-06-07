<h1 align="center">
  	<a href="spacelab.ufsc.br"><img src="https://github.com/spacelab-ufsc/golds-ufsc-doc/blob/master/figures/golds-ufsc-patch.png" alt="GOLDS-UFSC" width="30%"></a>
  	<br>
  	GOLDS-UFSC MISSION
  	<br>
</h1>

<h4 align="center">A compilation of the mission documents, diagrams, spreadsheets and figures.</h4>

<p align="center">
	<a href="">
		<img src="https://img.shields.io/badge/state-in%20development-lightgreen?style=for-the-badge">
	</a>
	<a href="">
		<img src="https://img.shields.io/badge/model-engineering-blue?style=for-the-badge">
	</a>
    <a href="http://golds.ufsc.br/en/team/">
		<img src="https://img.shields.io/badge/spacelab%20members-_-9cf?style=for-the-badge">
	</a>
    <a href="">
		<img src="https://img.shields.io/badge/other%20members-_-blueviolet?style=for-the-badge">
	</a>
	<a href="">
		<img src="https://img.shields.io/badge/partner-ufma-B44188?style=for-the-badge">
	</a>
	<a href="">
		<img src="https://img.shields.io/badge/partner-inpe-yellow?style=for-the-badge">
	</a>
	<a href="http://ufsc.br">
		<img src="https://img.shields.io/badge/sourced%20by-UFSC-orange?style=for-the-badge">
	</a>
	<a href="">
		<img src="https://img.shields.io/badge/sourced%20by-AEB-red?style=for-the-badge">
	</a>
	<a href="http://golds.ufsc.br">
		<img src="https://img.shields.io/badge/for%20more-here-lightgray?style=for-the-badge">
	</a>
</p>

<p align="center">
  	<a href="#overview">Overview</a> •
  	<a href="#mission-statement">Statement</a> •
  	<a href="#mission-objectives">Objectives</a> •
  	<a href="#mission-schedule">Schedule</a> •
  	<a href="#mission-requeriments">Requirements</a> •
  	<a href="#development-teams">Teams</a> •
  	<a href="#partners">Partners</a> •
  	<a href="#repository-organization">Repository</a> •
  	<a href="#licenses">Licenses</a> •
  	<a href="#notes">Notes</a>
</p>


## Overview

GOLDS-UFSC is a space technology demonstration mission created by the Federal University of Santa Catarina. The main goal is to provide the service module for the Environmental Data Collector (EDC) payload from INPE-RN. The service module was developed at UFSC and it has three main components: the Electric Power System (EPS), the On-Board Data Handling (OBDH) and Telemetry, Tracking and Command (TT&C).

Besides performing the EDC main functionalities, the mission will contribute to validating key technologies that will enable faster and cheaper development of future satellites reusing the same core structure. As an educational mission, it also serves to train engineering students in space mission conception, design, implementation and operation in all areas involved. 

It also acts as an experimenting platform for research in space technologies developed before, during, and after the operations phase of the mission, providing empirical data for experiments of many kinds. GOLDS-UFSC is expected to be launched by the end of 2020. Details of all systems developed for the mission are described in the documents listed in this repository in a top-level fashion and the detailed technical module documents in their respective repositories. This documentation structure is described in the <a href="#repository-organization">repository organization</a> section.



## Mission Statement

GOLDS-UFSC is a service module for INPE’s EDC payload, and also a platform for
the test of core spacecraft technologies in a microgravity, high-radiation and low Earth orbit
environment.



## Mission Objectives

1. To serve as a host platform for the EDC payload.
2. Validate the EDC payload in orbit.
3. Validate EDC functionality in orbit.
4. Validate core-satellite functions in orbit.
5. Evaluate the behavior of the core modules.
6. Perform experiments on radiation effects in electronic components in orbit.
7. Serve as relay for amateur radio communications.



## Mission Schedule

<img width="70%" src="https://github.com/spacelab-ufsc/golds-ufsc-doc/blob/master/figures/preliminary-schedule.png">



## Mission Requeriments

1. The power system shall be able to harvest solar energy.
2. The power system shall be able to store energy for use when GOLDS-UFSC is eclipsed.
3. The power system shall supply energy to all other modules.
4. The data handling system shall communicate with the other modules and store their data.
5. The communications system shall send a beacon signal periodically using VHF radio.
6. The communications system shall send the CubeSat telemetry using UHF radio.
7. The communications system shall be able to receive telecommands and respond to them accordingly.
8. The attitude system shall be able to perform a 1-axis stabilization of the CubeSat.
9. GOLDS-UFSC shall have the capability to receive and execute a shutdown telecommand, therefore ceasing all transmissions.
10. The downlink transmissions shall be done once at a time, either telemetry or beacon.
11. The ground station shall operate under the proper radio frequency communication licenses.
12. GOLDS-UFSC shall comply with international and Brazilian radio license agreements and restrictions.
13. The team shall build and operate a ground station for full communication with GOLDS-UFSC.



## Development Teams

Under definition!



## Partners

Under definition!




## Repository Organization

Under definition!



## Licenses

Under definition!



## Notes

### Dependencies

* ```latexmk```
* ```texlive-epstopdf```

### Generating the PDF file

```
make
```