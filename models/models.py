# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class rfid(models.Model):
    _name = 'barang'
    id_barang = fields.Char(string="ID", required=True)
    nama_barang = fields.Char(string="Nama Barang", required=True)


# url api intellifi live presence
# https://rfidindonesia.intellifi.nl/api/presences?key=9d0c13dc-fef4-4b94-af88-8bd237b628d7
api_url = "https://rfidindonesia.intellifi.nl/api/presences?key=9d0c13dc-fef4-4b94-af88-8bd237b628d7"
class rfidAPI(models.Model):
    _name = 'rfid.tag'
    hexcode = fields.Char(string="ID Tag")
    status = fields.Char(string="status tag")

    @api.multi
    def invoke_API(self):
        res = requests.get(api_url)
        print("Invoke API..")
        print(res)

        return res


class polybox(models.Model):
    _name = 'rfid.polybox'
    id_polybox = fields.Char(string="Hex Code Polybox", required=True)
    nama_polybox = fields.Char(string="Nama Polybox", required=True)
    status_polybox = fields.Selection([('terkirim', 'Polybag Terkirim'), ('tersedia', 'Polybog Tersedia')], default='tersedia', required=True)
    tgl_kirim = fields.Date(string="Tanggal Kirim Polybox")
    tgl_masuk = fields.Date(string="Tanggal Masuk Polybox")
    listProduct = fields.Integer(string="Jumlah Produk")
    deskripsi = fields.Char(string="Deskripsi Polybox")






#class rfid(models.Model):
	#_name = "rfid.barang"
	#3id_barang = fields.Char(string='ID' , required=True)
	#nama_barang = fields.Char(string='Nama Barang', required=True)
	

