#!/usr/bin/env bash

az webapp up -n fmlapp

az webapp log tail
