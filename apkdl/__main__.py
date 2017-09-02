from apkdl.dl import download, search, APPS
import sys

def main():
	if len(sys.argv) > 1:
		query = " ".join(sys.argv[1:])

		print('Searching for: {}'.format(query))

		search(query)

		if len(APPS) > 0:
			for idx, app in enumerate(APPS):
				print("""[{:02d}] {}\n     Developer: {}""".format(idx, app[0], app[1]))
				print('=========================================')

			option = ""
			while option == "":
				option = input('Which app would you like to download?\n> ')
				try:
					if 0 <= int(option) < len(APPS):
						option = int(option)
					else:
						print('That was not a valid option')
						option = ""
				except ValueError:
					option = ""

			print('Downloading {}.apk ...'.format(APPS[option][2].split('/')[-1]))

			download(APPS[option][2])

			print('Download completed!')
		else:
			print('No results')
	else:
		print('Missing input! Try:')
		print('apkdl [app name]')