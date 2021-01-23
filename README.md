<h1 align="center">
  	<a href="spacelab.ufsc.br"><img src="https://github.com/spacelab-ufsc/golds-ufsc-doc/blob/master/figures/golds-ufsc-patch.png" alt="GOLDS-UFSC" width="30%"></a>
  	<br>
  	GOLDS-UFSC MISSION
  	<br>
</h1>

<h4 align="center">A compilation of the mission documents, diagrams, spreadsheets and figures.</h4>

<p align="center">
	<a href="https://github.com/spacelab-ufsc/spacelab#versioning">
		<img src="https://img.shields.io/badge/status-in%20development-red?style=for-the-badge">
	</a>
    <a href="http://golds.ufsc.br/en/team/">
		<img src="https://img.shields.io/badge/spacelab%20members-8-blue?style=for-the-badge">
	</a>
	<a href="">
		<img src="https://img.shields.io/badge/partner-inpe--rn-yellow?style=for-the-badge">
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
  	<a href="#repositories-organization">Repositories</a> •
  	<a href="#partners">Partners</a> •
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

| Start [+months]  | Finish [+months] | Activity / Phase                                                                                          |
|------------------|------------------|-----------------------------------------------------------------------------------------------------------|
| T0               | T0 + 4           | Acquisition and manufacturing of critical elements and components for the platform                        |
| T0               | T0 + 4           | Acquisition and manufacture of elements and components critical to the payload                            |
| T0               | T0 + 9           | Acquisition and manufacturing of critical elements and components for the solo segment                    |
| T0               | T0 + 6           | Compatibility tests between platform and payload in SpaceLab UFSC                                         |
| T0 + 4           | T0 + 10          | Integration of the engineering model in SpaceLab UFSC                                                     |
| T0 + 4           | T0 + 11          | Preparation and suitability of the ground segment                                                         |
| T0 + 8           | T0 + 10          | Verification and validation of the engineering model at SpaceLab UFSC                                     |
| T0 + 8           | T0 + 11          | Verification and validation of the flight model at SpaceLab UFSC                                          |
| T0 + 9           | T0 + 12          | Data collection platforms installation                                                                    |
| T0 + 10          | T0 + 11          | Verification and validation tests of Engineering Model compatibility with EMMN in the INPE / CRN in Natal |
| T0 + 10          | T0 + 11          | Environmental tests at the Integration and Testing Laboratory (LIT / INPE)                                |
| T0 + 11          | T0 + 11          | Flight model acceptance and ground segment review                                                         |
| T0 + 9           | T0 + 12          | Ground segment delivery                                                                                   |
| T0 + 11          | T0 + 12          | Flight model delivery                                                                                     |


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




## Repositories Organization

Under definition!



## Partners

#### SpaceLab

#### INPE-RN

#### AEB



## Licenses

The SpaceLab follows a strong open-source approach in order to encourage and promote knowledge. Then, refer to the LICENSE file in the GitHub page for each repository. This mission uses different open-source licenses accordingly to projects needs and restrictions. It is used GNU General Public License v3.0 for firmware sources, CERN Open Hardware License v2.0 for hardware files, and CC BY-SA 4.0 for the documentation. Some third-part files and libraries are subjected to their specific terms and licenses. Please, double check licenses and third-part components used with other licenses, since restrictions might apply.


## Notes

This repository includes the sources of the main documentation. In order to edit/compile/generate, check the following:  

#### Dependencies

* ```latexmk```
* ```texlive-epstopdf```

#### Generating the PDF file

```
make
```








