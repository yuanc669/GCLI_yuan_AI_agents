/*
 * PAS Mesangial Expansion Quantitative Analysis Macro (DN_GaExo Project)
 * 
 * Logic:
 * 1. User provides a set of glomerular images (cropped or whole field).
 * 2. Macro prompts user to draw ROI for Glomerular Tuft (if not already cropped).
 * 3. Color Deconvolution [H PAS] isolates the pink/red mesangial matrix.
 * 4. Thresholding identifies PAS-positive area.
 * 5. Results (Tuft Area, PAS Area, Mesangial Index %) are saved.
 */

macro "Analyze PAS Mesangial Expansion" {
    
    // Setup
    run("Set Measurements...", "area mean integrated limit display redirect=None decimal=3");
    
    // Folder selection
    input = getDirectory("Choose Image Folder (PAS Glomeruli)");
    output = getDirectory("Choose Output Folder for Results");
    list = getFileList(input);
    
    // Results Table initialization
    f = File.open(output + "PAS_Mesangial_Results.csv");
    print(f, "Sample_Name,Glomerulus_ID,Tuft_Area,PAS_Area,Mesangial_Index_Percent");
    
    setBatchMode(false); // Manual ROI selection requires batch mode OFF

    for (i = 0; i < list.length; i++) {
        if (endsWith(list[i], ".tif") || endsWith(list[i], ".jpg") || endsWith(list[i], ".png")) {
            open(input + list[i]);
            imgName = getTitle();
            
            // Step 1: Manual ROI Selection (User selects the Glomerular Tuft)
            setTool("freehand");
            waitForUser("Draw a ROI around the Glomerular Tuft, then click OK.");
            
            if (selectionType() == -1) {
                print("No selection made for " + imgName + ". Skipping.");
                close();
                continue;
            }
            
            run("Add to Manager");
            roiManager("select", 0);
            getStatistics(tuftArea);
            
            // Step 2: Color Deconvolution
            // We use the H-PAS vector. 
            // Channel 2 is usually the PAS (pink/red) channel.
            run("Colour Deconvolution", "vectors=[H PAS]");
            
            // Identify and select the PAS Channel (usually the second one)
            selectWindow(imgName + "-(Colour_2)"); 
            roiManager("select", 0);
            
            // Step 3: Thresholding (Optimized for PAS)
            setThreshold(0, 140); // Standard starting point, may need user adjustment
            run("Convert to Mask");
            
            // Measure PAS Area within the Tuft ROI
            run("Analyze Particles...", "size=5-Infinity show=Nothing display exclude include summarize");
            pasArea = getResult("Area", nResults - 1); // Get the latest measurement
            
            // Step 4: Data Calculation
            mesangialIndex = (pasArea / tuftArea) * 100;
            
            // Log to CSV
            print(f, imgName + "," + (i+1) + "," + tuftArea + "," + pasArea + "," + mesangialIndex);
            
            // Save Mask for QC
            saveAs("Png", output + imgName + "_Mask.png");
            
            // Cleanup
            close(imgName + "-(Colour_1)");
            close(imgName + "-(Colour_2)");
            close(imgName + "-(Colour_3)");
            close(imgName);
            roiManager("delete");
            run("Clear Results");
        }
    }
    
    File.close(f);
    print("Analysis Complete! Results saved to: " + output);
}
