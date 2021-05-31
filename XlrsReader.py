import xlrd

def GetData():
    # Open the xls file containing the base data
    workbook = xlrd.open_workbook(r"GraphesRobot.xls")

    # get sheet using its name
    # sheet = workbook.sheet_by_name("Sheet")

    # Getting the first sheet
    sheet = workbook.sheet_by_index(0)

    # Print all sheet names
    # for sh in workbook.sheets():
    #     print(sh.name)

    # Display number of vertices (row 0 col 0 to ?)
    header = sheet.row_values(0, start_colx=0, end_colx=None)

    # row_slice returns the cell object(both data type and value) in case you also need to check the data type
    # row_1 = sheet.row_slice(1, start_colx=0, end_colx=None)

    row_count = sheet.nrows
    col_count = sheet.ncols

    # display the content of the sheet
    # for cur_row in range(0, row_count):
    #     for cur_col in range(0, col_count):
    #         cell = sheet.cell(cur_row, cur_col)
    #         print("row: {} - col: {} - Cell Value {}
    #         - Cell type: {}".format(cur_row, cur_col, cell.value, cell.ctype))

    # Load the vertices into a new dict variable.
    # Vertices are defined in row 1, columns 1 to max vertices
    # Coordinates of each vertex are in the 3 next lines under same column number
    vertices = dict()
    for cur_col in range(1, int(header[1])+1):
        vertices[sheet.cell(1, cur_col).value] =\
            {
                str(sheet.cell(2, 0).value): int(sheet.cell(2, cur_col).value),
                str(sheet.cell(3, 0).value): int(sheet.cell(3, cur_col).value),
                str(sheet.cell(4, 0).value): int(sheet.cell(4, cur_col).value),
            }

    # print("Vertex coordinates:")
    # for vertex in vertices:
    #     # Display vertex coordinates
    #     x, y, z = None, None, None
    #     for key, value in vertices[vertex].items():
    #         if key == 'x':
    #             x = value
    #         elif key == 'y':
    #             y = value
    #         elif key == 'z':
    #             z = value
    #     print("Vertex {}: ({},{},{})".format(vertex, x, y, z))

    # Create the edges from the sheet (starts at row 5 until end of the sheet)
    edges = dict()
    for cur_row in range(5, row_count-2):
        # Get the source and target vertex
        # Col 1 is the source, col 2 is the target
        src = str(sheet.cell(cur_row, 1).value)
        tgt = str(sheet.cell(cur_row, 2).value)
        # Test if edge already exists
        if src not in edges:
            # Add the edge and the first target found
            edges[src] = [tgt]
        else:
            # Add the new target to the edge
            edges[src].append(tgt)

    # Load the Departure vertex and Arrival vertex
    departure = str(sheet.cell(row_count-2, 1).value)
    arrival = str(sheet.cell(row_count-1, 1).value)

    # Display Departure and Arrival
    print(' ')
    print("Departure: ",end='')
    print(departure)
    print(' ')
    print("Arrival: ",end='')
    print(arrival)
    print(' ')

    return vertices,edges,departure,arrival