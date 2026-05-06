/*
 * H&E Glomerular Hypertrophy Analysis Macro (DN_GaExo Project)
 * 
 * Goal: Measure the Cross-sectional Area of Glomerular Tufts on H&E stains.
 * Glomerular hypertrophy is a key characteristic of early-to-mid stage DN.
 */

macro "Analyze H&E Glomerular Area" {
    
    // Setup
    run("Set Measurements...", "area perimeter circularity display redirect=None decimal=3");
    
    input = getDirectory("Choose Folder containing H&E Glomeruli Images");
    output = getDirectory("Choose Output Folder for Results");
    list = getFileList(input);
    
    // Results Table
    f = File.open(output + "HE_Glomerular_Area_Results.csv");
    print(f, "Sample_Name,Glomerulus_ID,Tuft_Area,Perimeter,Circularity");
    
    setBatchMode(false); 

    for (i = 0; i < list.length; i++) {
        if (endsWith(list[i], ".jpg") || endsWith(list[i], ".png") || endsWith(list[i], ".tif")) {
            open(input + list[i]);
            imgName = getTitle();
            
            // Step 1: Manual ROI Selection (Glomerular Tuft)
            setTool("freehand");
            waitForUser("Draw a ROI around the Glomerular Tuft, then click OK.");
            
            if (selectionType() == -1) {
                print("No selection for " + imgName);
                close();
                continue;
            }
            
            // Step 2: Measure
            run("Measure");
            area = getResult("Area", nResults - 1);
            perim = getResult("Perim.", nResults - 1);
            circ = getResult("Circ.", nResults - 1);
            
            // Step 3: Log Data
            print(f, imgName + "," + (i+1) + "," + area + "," + perim + "," + circ);
            
            // Optional: Save Overlay
            run("Flatten");
            saveAs("Jpeg", output + imgName + "_Measured.jpg");
            
            close(); // Close flatten
            close(imgName); // Close original
        }
    }
    
    File.close(f);
    print("H&E Glomerular Hypertrophy Analysis Complete.");
}
